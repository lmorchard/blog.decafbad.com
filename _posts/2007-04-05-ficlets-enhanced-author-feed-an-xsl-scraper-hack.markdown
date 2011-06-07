--- 
wordpress_id: 1046
layout: post
title: Ficlets enhanced author feed, an XSL scraper hack
wordpress_url: http://decafbad.com/blog/2007/04/05/ficlets-enhanced-author-feed-an-xsl-scraper-hack
---
I've been trying to get myself serious about writing and even set up a [personal slush pile for my output](http://decafbad.com/skein/).  Then, I found [Ficlets][], and spewed a few quick starter stories there.  And then... I stopped.  I'm hoping to pick it up again very soon, but I guess that's the nature of my [serial enthusiasm](http://decafbad.com/blog/2006/05/26/confessions-of-a-serial-enthusiast)—it doesn't just apply to hacking.

So, here's something ironic:  I just spent a few hours tonight throwing together a hack for [Ficlets][].  See, [Ficlets][] runs on original stories, comments, ratings, and sequels and prequels to stories.  You can get an Atom feed of an author's stories and a feed of comments—but it seems like there's no way to get notified of prequels and sequels, which are a very gratifying part of the whole shebang.

With that in mind, check out this RSS feed:

   * [`http://decafbad.com/2005/12/FeedMagick/www-bin/ficlets.php?author=l_m_orchard`](http://decafbad.com/2005/12/FeedMagick/www-bin/ficlets.php?author=l_m_orchard)

That's a blend of all my stories, comments on my stories, as well as prequels and sequels found for my stories.  Subscribing to that feed will give me updates whenever there's anything new in all the above.  It's thrown together using a semi-crazy mix of my [FeedMagick][] package for caching, and some XSL for scraping.  If you'd like a feed like this of your own, just replace `l_m_orchard` for your own author name in the `author` parameter.

**Please note, however, that this little service is hosted on my site and may go away at any time for any reason.**

In case you're interested in what's under the hood, here's the quick and dirty XSL that's behind it:

   * [`http://decafbad.com/2007/04/ficlets.xsl`](http://decafbad.com/2007/04/ficlets.xsl)

This thing's made possible because the [Ficlets][] feeds are XML, **and so are the XHTML pages happily infested with microformats**.  If they ever go invalid, this scraper breaks.  But, that's the nature of scrapers, and it works for now.  Oh, and although they provide Atom, this feed is RSS 2.0.  Why?  Because it was easier that way.  I might put some more effort into an Atom feed, but my itch has so far been scratched.

[FeedMagick]: http://decafbad.com/trac/wiki/FeedMagick
[ficlets]: http://ficlets.com/authors/l_m_orchard
