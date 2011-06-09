--- 
wordpress_id: 710
layout: post
title: Trac rocks like a really rocking thing
date: "2005-09-30T12:11:09-04:00"
tags: 
- asides
- projects
- python
- decafbad
- trac
wordpress_slug: trac-rocks-like-a-really-rocking-thing
wordpress_url: http://decafbad.com/blog/?p=710
---
Say hello to [my new Trac installation][dbtrac]!

For a couple of years now, I've been meaning to take a serious look at [Trac][].  But, general level of busy, as well as random obstacles to getting it up and running kept me from getting very far.  Such is so often the story with me.

Finally, though, I've gotten [an instance][dbtrac] running on our server here.  All I can say is, "**Wow!**"  This package does everything I ever wanted to cobble together using [TWiki][twiki], [MoinMoin][moin], [kwiki][] [viewcvs][], and any other pieces I ever looked at (ie. [Bugzilla][], [Request Tracker][], etc)

[Trac][] has an amazingly dead-simple macro and plugin system which puts [TWiki][] and possibly [kwiki][] to shame.  Just take a look at the [MacroBazzar][baz] and this [hacks collection][hacks].  And, the system seems pretty cleanly architected—templates pages, simple extension points, SQLite database.  I've already been able to easily wade in and make some tweaks of my own under the hood, as well as fix a few macro/plugins which were broken between v0.8 / v0.9 revisions.

Your mileage may vary, of course, but I think I've found my new favorite web app.  It's now a replacement for the wiki and SVN repository browser I used to have running on 0xDECAFBAD v3.

[moin]: http://moinmoin.wikiwikiweb.de/
[kwiki]: http://www.kwiki.org/
[baz]: http://projects.edgewall.com/trac/wiki/MacroBazaar
[hacks]: http://trac-hacks.swapoff.org/
[tag]: http://dev.muness.textdriven.com/trac.cgi/wiki/tags/Setup
[request tracker]: http://www.bestpractical.com/rt/
[bugzilla]: http://www.bugzilla.org
[twiki]: http://twiki.org/
[viewcvs]: http://viewcvs.sourceforge.net/
[dbtrac]: http://decafbad.com/trac/
[trac]: http://projects.edgewall.com/trac/
