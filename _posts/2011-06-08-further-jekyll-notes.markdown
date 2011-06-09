---
layout: post
title: "Further Jekyll notes"
tags: [ jekyll, metablogging, github ]
published: true
time: 5:46PM
---

**TL;DR**: This is an in-progress entry, where I plan to collect some notes on how I've
set up and am using Jekyll. I may call it "done" at some random point and
publish it. I may even subsequently update it from time to time, after that.

* To speed up the authoring / previewing cycle on my laptop, I move all but this
  years' posts into a `_posts_archived` folder and don't commit the change.
    * Kind of a pain; feels like I'm Doing It Wrong.

* [Github Pages][pages] seems interesting, but I don't think it's right for me.
    * My plugins don't run, so my tag pages aren't created.
        * [davedash][] has a different approach for this, though.
    * I can't get the permalinks just the way I like them
    * I'd have to set a `CNAME` in my DNS to point at a subdomain (ie.
      `blog.decafbad.com`), because I don't want to delegate my entire root
      domain over to GitHub.
    * I would 100% totally use [GitHub Pages][pages] for another project that
      I'm starting from scratch, though.

* Since related posts via LSI is such a bear, I may try doing something with
  tags. That is: 
    * take all the tags from a post;
    * find the 5 latest posts for each tag;
    * display the unique set of posts

* I want my permalinks to look like `/2011/06/08/slug`
    * Not `/2011/06/08/slug/` or `/2011/06/08/slug.html`
    * Look, ma, no trailing slash!
    * This is the way I've had my URLs for years, and I want to maintain my URLspace.
    * And I also don't want every URL missing a trailing slash to get bounced
      with a `301 Moved Permanently` to the equivalent *with* a trailing
      slash. That's bogus.
    * So, I'm using the `pretty` permalinks setting, and I have this in my
      nginx config:
        * `if (-f $request_filename/index.html) { rewrite ^(.+)$ $1/index.html last; }`
      
[pages]: http://pages.github.com/
[davedash]: https://github.com/davedash/davedash.github.com
