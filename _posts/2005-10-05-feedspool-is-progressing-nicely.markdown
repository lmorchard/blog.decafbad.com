--- 
wordpress_id: 717
layout: post
title: FeedSpool is progressing nicely
date: "2005-10-05T16:58:21-04:00"
tags: 
- webdev
- rss
- syndication
- atom
- projects
- aggregation
- feedspool
wordpress_slug: feedspool-is-progressing-nicely
wordpress_url: http://decafbad.com/blog/?p=717
---
I'm at it again:  Last night, I got an initial stab at a [plugin API][api] for [FeedSpool][fs] working.

The first thing I built was an [auto-adjusting feed poll schedule plugin][vary] which varies the time between feed polls based on whether there were new entries found in the latest poll.  It's kind of like an AIMD algorithm used in networking—I thank [Gnomon][g] for the idea a few years back.

The next thing I built was a [quick plugin bundle I call `miniagg`][mini].  If you'd like a preview, I've posted [an HTML snapshot of what `miniagg` produces][mini_preview].  It's a refinement and reworking of various aggregator UI pieces I've had floating around since [AmphetaOutlines][amph], only I think this is the simplest and cleanest I've gotten it yet.  (CSS and unobtrusive JavaScript, hooray!)

This only seems to work on Firefox and Safari—it's currently broken for MSIE, and I don't care enough to fix it yet.  (Something to do with multiple CSS classes, I believe.)  But, if you're unfortunate enough to be using that browser, here's a screen capture:  

<a href="http://www.decafbad.com/blog_attachments/miniagg-1.jpg" onclick="window.open('http://www.decafbad.com/blog_attachments/miniagg-1.jpg','popup','width=984,height=742,scrollbars=no,resizable=yes,toolbar=no,directories=no,location=no,menubar=no,status=yes,left=0,top=0');return false"><img src="http://www.decafbad.com/blog_attachments/miniagg-1-tm.jpg" height="244" width="324" border="1" hspace="4" vspace="4" alt="Miniagg-1" /></a>

[g]: http://decafbad.com/blog/2003/09/29/dynamic-polling-freq-too#comment-1061
[amph]: http://decafbad.com/trac/wiki/AmphetaOutlines
[vary]: http://decafbad.com/trac/browser/trunk/feedspool/plugins/poll_schedule_vary.py
[api]: http://decafbad.com/trac/wiki/FeedSpool/Plugins
[fs]: http://decafbad.com/trac/wiki/FeedSpool
[mini]: http://decafbad.com/trac/browser/trunk/feedspool/plugins/miniagg/
[mini_preview]: http://decafbad.com/2005/10/miniagg/news-20051005-152956.html
