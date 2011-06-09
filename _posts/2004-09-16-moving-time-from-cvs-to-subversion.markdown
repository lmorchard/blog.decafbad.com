--- 
wordpress_id: 548
layout: post
title: "Moving time: From CVS to Subversion"
excerpt: So, I'm waiting for the other shoe to drop.  After making sure things seemed reasonably stable post-server-move, I migrated my CVS repository here to Subversion.
date: "2004-09-16T11:29:04-04:00"
tags: 
- syndication
- xml
wordpress_slug: moving-time-from-cvs-to-subversion
wordpress_url: http://www.decafbad.com/blog/?p=548
---
So, I'm waiting for the other shoe to drop.  After making sure things seemed reasonably stable post-server-move, I migrated my CVS repository here to [Subversion][subversion].  There were one or two tiny bumps in the road-- such as a default setting in Apache to deny access to anything starting with .ht (ie. .htaccess)-- but so far, so good.  [ViewCVS][viewcvs] appears to support Subversion, and I've also discovered an alternate frontend called [WebSVN][websvn].  I like ViewCVS better, but WebSVN offers RSS feeds on commits.

One consequence to this move is that soon, when I take down everything related to CVS, I'll have plenty of broken links (since I frequently link to ViewCVS pages for my projects).  So, I think my next step will be to set up some redirects to a reasonable number of things for continuity's sake.

So, anyway... if you've been keeping up with `dbagg3`, the action's not in CVS anymore.  It's here:

* <http://www.decafbad.com/svn/trunk/dbagg3/>

Alternately, you can also peek at things here:

* <http://www.decafbad.com/svn-view/trunk/dbagg3/>
* [WebSVN](http://www.decafbad.com/websvn/listing.php?repname=0xDECAFBAD%20projects&#38;path=%2Ftrunk%2Fdbagg3%2F&#38;rev=0&#38;sc=0)

(Can you see one reason why I like ViewCVS so much better?)

[viewcvs]: http://viewcvs.sourceforge.net/
[subversion]: http://subversion.tigris.org/
[websvn]: http://websvn.tigris.org/
