--- 
wordpress_id: 1019
layout: post
title: XoxoOutliner and further outline addressing adventures
wordpress_url: http://decafbad.com/blog/2006/11/15/xoxooutliner-and-further-outline-addressing-adventures
---
[Revised the addressing code a bit][rev], adding a few new kinds of addresses and getting ready to support sub-outline *updates*.  That is, fetch a sub-branch of an outline and then later post a change to that sub-branch using the same address.  Needs more thought - ie. what happens if things move between fetch and update? - but here are a few more samples:

* First is a straight linear index counting down from the top of the outline:
   * [http://decafbad.com/2006/11/XoxoOutliner/outlines/README;index:4?format=xoxo](http://decafbad.com/2006/11/XoxoOutliner/outlines/README;index:4?format=xoxo)
* Second is a navigation of outline structure, alternating numbers and letters:
   * [http://decafbad.com/2006/11/XoxoOutliner/outlines/README;level:3c4?format=xoxo](http://decafbad.com/2006/11/XoxoOutliner/outlines/README;level:3c4?format=xoxo)

That's all for now.  In my next round of enthusiasm, I may try stealing [Tom Morris' Opath idea][opath]...

[rev]: http://decafbad.com/trac/changeset/779
[opath]: http://blogs.opml.org/tommorris/2006/11/11#opathAToolToPopulariseAConcept
