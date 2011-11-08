#!/usr/bin/env python
"""This is a dirty, dirty script that harvests comment threads from Disqus for
ancient blog posts and archives the comments directly into the post source."""

import sys
import os
import os.path
import glob
import datetime
import urllib
import urlparse
import shelve
import json
import cgi
import pprint

import disqusapi
import yaml
import isodate
import pytz

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import settings

pp = pprint.PrettyPrinter(depth=6)

USE_CACHE = getattr(settings, 'USE_CACHE', False)

POSTS_JSON = os.path.join(settings.DATA_DIR, 'posts.json')
THREADS_JSON = os.path.join(settings.DATA_DIR, 'threads.json')
COMMENTS_JSON = os.path.join(settings.DATA_DIR, 'comments.json')

TEMPLATES = {

    # I wish this was a <section>. But, Markdown doesn't recognize it as a
    # block element, and so content within gets munged.
    "root": """<div id="comments" class="comments archived-comments">
            <h3>Archived Comments</h3>
            %(comments|safe)s
        </div>
    """,

    "comments": u"""
        <ul class="comments">
            %(comments|safe)s
        </ul>
    """,

    "comment": u"""
        <li class="comment" id="comment-%(id)s">
            <div class="meta">
                <div class="author">
                    <a class="avatar image" rel="nofollow" 
                       href="%(author.url)s"><img src="%(author.avatar.permalink)s"/></a>
                    <a class="avatar name" rel="nofollow" 
                       href="%(author.url)s">%(author.name)s</a>
                </div>
                <a href="#comment-%(id)s" class="permalink"><time datetime="%(createdAt)s">%(createdAt)s</time></a>
            </div>
            <div class="content">%(raw_message|safe)s</div>
            %(comments_rendered|safe)s
        </li>
    """
}

TEMPLATES.update(getattr(settings, 'DISQUS_ARCHIVE_TEMPLATES', {}))


def main():
    """Main driver. Let's do this thing"""
    disqus = disqusapi.DisqusAPI(settings.DISQUS_SECRET_KEY,
                                 settings.DISQUS_PUBLIC_KEY)

    # First, fetch and parse all Jekyll posts
    if USE_CACHE and os.path.exists(POSTS_JSON):
        posts_by_url = json.load(open(POSTS_JSON))
    else:
        posts_by_url = load_all_posts()
        save_json(POSTS_JSON, posts_by_url)

    # Second, fetch all Disqus threads
    if USE_CACHE and os.path.exists(THREADS_JSON):
        threads = json.load(open(THREADS_JSON))
    else:
        threads = fetch_threads(disqus)
        save_json(THREADS_JSON, threads)
    
    # Third, fetch all comments for threads, associate with posts
    fetch_comments_for_posts(disqus, posts_by_url, threads)

    # Finally, archive each post's comment thread into post source.
    now = datetime.datetime.utcnow()
    cutoff_dt = (now - settings.MAX_POST_AGE).isoformat()
    for post in posts_by_url.values():
        if post['meta'].get('comments_archived', False):
            # Skip posts already archived
            continue
        if post['pub_date'] > cutoff_dt:
            # Skip any posts newer than the cutoff date
            continue
        archive_comments_to_post(post)


def save_json(path, data):
    """Save JSON to a path, possibly creating parent directories first."""
    dirp = os.path.dirname(path)
    if not os.path.isdir(dirp):
        os.makedirs(dirp)
    json.dump(data, open(path, 'w'))
    print "\tWrote %s" % path


def load_all_posts():
    """Load up all posts, parsing metadata and mapping by URL"""
    print "Loading posts..."
    posts_by_url = dict()
    posts_list = glob.glob(os.path.join(settings.POSTS_DIR, '*.markdown'))
    for post_path in posts_list:
        if not os.path.isfile(post_path):
            continue
        (full_url, path, fn, pub_date, meta, post) = fetch_post(post_path)
        posts_by_url[full_url] = p = {
            "url": full_url,
            "pub_date": pub_date.isoformat(),
            "fn": fn,
            "meta": meta,
            "post": post
        }
    print "Loaded %s posts" % len(posts_by_url)
    return posts_by_url

    
def fetch_post(post_path):
    """Given the path to a post, fetch it and parse out some metadata"""
    (path, fn) = os.path.split(post_path)
    
    # HACK: Can't use yaml.load_all(), because the post part isn't YAML.
    (meta_lines, post_lines, boundary_ct) = [], [], 0
    fin = open(post_path, 'r')
    lines = fin.readlines()
    for line in lines:
        if line.startswith("---"):
            boundary_ct += 1
        elif boundary_ct == 1:
            meta_lines.append(line)
        else:
            post_lines.append(line)
    meta, post = yaml.load("".join(meta_lines)), "".join(post_lines)

    # FIXME: I was high as a kite when I wrote this date handling code:
    parts = fn.split('-', 3)
    if 'date' in meta:
        if type(meta['date']) is datetime.datetime:
            pub_date = meta['date']
            meta['date'] = meta['date'].isoformat()
        else:
            pub_date = (isodate.parse_datetime(meta['date'])
                               .replace(tzinfo=None))
    else:
        pub_date = (isodate.parse_datetime('%s-%s-%sT00:00:00Z' % (
                                          parts[0], parts[1], parts[2]))
                           .replace(tzinfo=None))

    url = '/'.join(['%04d' % pub_date.year, 
                    '%02d' % pub_date.month,
                    '%02d' % pub_date.day, 
                    parts[3]]).replace('.markdown', '')
    full_url = urlparse.urljoin(settings.BASE_URL, url)

    return (full_url, path, fn, pub_date, meta, post)


def fetch_threads(disqus):
    """Fetch all threads from Disqus"""
    print "Fetching threads..."
    result = disqusapi.Paginator(disqus.forums.listThreads, **{
        "forum": settings.DISQUS_FORUM,
        # TODO: Uncomment this, let Disqus control thread open/close
        #"include": "closed", 
        "order": "desc",
    })
    threads = [x for x in result]
    print "Fetched %s threads" % len(threads)
    return threads


def fetch_comments_for_posts(disqus, posts_by_url, threads):
    """Fetch comments for each post's respective thread"""
    now = datetime.datetime.utcnow()
    cutoff_dt = (now - settings.MAX_POST_AGE).isoformat()

    for thread in threads:

        if thread['posts'] and thread['link'] in posts_by_url:
            post = posts_by_url[thread['link']]

            if post['pub_date'] > cutoff_dt:
                # Skip any posts newer than the cutoff date
                continue

            if post['meta'].get('comments_archived', False):
                # Skip posts for which comments have already been archived.
                continue

            # Check if there's already JSON for these comments
            path = os.path.join(settings.DATA_DIR, 'comments/%s.json' % post['fn'])
            if USE_CACHE and os.path.exists(path):
                continue

            comments = [x for x in disqusapi.Paginator(
                disqus.threads.listPosts, **{
                    "forum": settings.DISQUS_FORUM,
                    "thread": thread['id']
                })]
            print "Got %s comments from disqus" % len(comments)

            save_json(path, comments)


def archive_comments_to_post(post):
    """Render comment thread from a post onto the end of the content,
    reconstitute the source file with altered YAML front matter."""
    fn = os.path.join(settings.POSTS_DIR, post['fn'])

    print "Archiving to %s" % fn
    
    post['meta']['comments_archived'] = True
    out = [
        u"---\n",
        unicode(yaml.safe_dump(post['meta'],
            width=70, indent=4, default_flow_style=False)),
        u"---\n",
        unicode(post['post']),
    ]

    path = os.path.join(settings.DATA_DIR,
                        'comments/%s.json' % post['fn'])
    if not os.path.exists(path):
        print "\tNo comments found for %s" % post['fn']
    else:
        comments = json.load(open(path))
        print "\t%s comments found for %s" % (len(comments), 
                                              post['fn'])
        out.extend([
            u"\n",
            render_comments_for_post(comments)
        ])

    open(fn, 'w').write(u"".join(out).encode('utf-8'))


def render_comments_for_post(comments):
    """Render the hierarchical comment thread for a post"""
    # Index the posts by ID
    by_id = dict((str(x['id']), x) for x in comments)

    # Build the thread hierarchy from parent ID pointers.
    for comment in comments:
        if comment['parent']:
            parent = by_id[str(comment['parent'])]
            if 'comments' not in parent:
                parent['comments'] = []
            parent['comments'].append(comment)

    # Grab the root comments, which have no parents.
    root_comments = [x for x in comments if x['parent'] is None]

    # Fire up the template turbines.
    return (TEMPLATES['root'] % HTMLTemplateData({
        "comments": render_comment_list(root_comments)
    }))


def render_comment_list(comments):
    """Render a list of comments, recursively rendering child comments"""

    comments = sorted(comments,
                      lambda x,y: cmp(x['createdAt'], y['createdAt']))

    # First, render comments for any child comments.
    for c in comments:
        if c.has_key('comments'):
            c['comments_rendered'] = render_comment_list(c['comments'])

    # Then, render the list of comments.
    return TEMPLATES['comments'] % HTMLTemplateData({
        "comments": "".join(TEMPLATES['comment'] % HTMLTemplateData(x)
                            for x in comments)
    })


class HTMLTemplateData(dict):
    """Quick and dirty utility for populating an HTML template with a dict"""

    ENCODERS = {
        "html": lambda x: cgi.escape(unicode(x)),
        "safe": lambda x: unicode(x),
    }

    def __init__(self, d, encoder=None):
        self.__dict__ = d
        self.encoder = encoder or self.ENCODERS['html']

    def set_encoder(self, name):
        self.encoder = self.ENCODERS.get(name, self.ENCODERS['html'])

    def encode(self, val):
        return self.encoder(val)

    def __getitem__(self, key):

        if '|' in key:
            # "|" indicates an encoder change.
            key, encoder_name = key.split('|', 1)
            self.set_encoder(encoder_name)

        if '.' in key:
            # "." navigates dict data structure.
            key, s_key = key.split('.', 1)
            s_val = self.__dict__[key]
            if isinstance(s_val, dict):
                return HTMLTemplateData(s_val, self.encoder)[s_key]
            else:
                return self.encode(s_val)

        val = self.__dict__.get(key, '')
        return self.encode(val)


if __name__ == "__main__":
    # Let the driver take over from here.
    main()
