--- 
wordpress_id: 1937
layout: post
title: Firefox Sync server on Google App Engine
wordpress_url: http://decafbad.com/blog/?p=1937
---
<em><strong>TL;DR:</strong> [I built an implementation][impl] of the [Firefox Sync server API][api10] for [Google App Engine][appengine].</em>

[impl]: http://github.com/lmorchard/firefox-sync-appengine
[api10]: https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API
[appengine]: http://appengine.google.com/

<a href="http://www.mozilla.com/en-US/firefox/sync/" style="float: right; padding: 0 0 0em 0em; display: block; text-decoration: none; border: none"><img src="http://mozcom-cdn.mozilla.net/img/firefox/sync/sync-background.png" style="border: none" /></a>

To celebrate [Independence Day][july4], I figured I might take a shot at liberating [Firefox Sync][sync] from the tyranny of [Mozilla's servers][servers]. 

Thus, over the past few days, I've [built a sync server][impl] using the [1.0 Sync API][api10], hosted on [Google App Engine][appengine].

I lied about the *tyranny* thing, thoughâ€”I just wanted to say something clever about the holiday. In reality, with respect to [Firefox Sync][sync], Mozilla has done all of the following:

1. Published [the Sync API spec][api10];
2. Released [the source code for the server used in-house][sync-server];
3. Explicitly included the option to use a custom server when setting up sync in the browser.

This means that, although Mozilla offers servers to go along with [Firefox Sync][sync], you're totally free to take your data elsewhere. Since your sync data is encrypted and practically opaque to the server, there's no direct profit for Mozilla in offering free sync hostingâ€”not even through any clandestine data mining for devious purposes. It's just that sync makes Firefox a better browser, and *somebody* has to run some servers to make it work.

So, there's every incentive to make it easy for you to switch sync providers and *stop freeloading* on Mozilla's servers. Building a server on [Google App Engine][appengine] means I can freeload on *Google's* servers!

I kid, of course. No one's really complaining about freeloaders, and App Engine has quotas in place to head off any serious moochingâ€”which is why I'm not telling you where to find *my* sync server deployed on Google App Engine, by the way. 

No, I did this because:

* Firefox Sync and Google App Engine are interesting and important technologies;
* I've already done a bit of work on the PHP-based Firefox Sync server at Mozilla;
* I really wanted to take a break from PHP and spend some time with my old friend Python.

There are, of course, a number of bugs in this server. But, it seems to be working between a number of machines and browser profiles I have at home. Things are really in need of optimization, it suffers from my inexperience with App Engine, and I keep running into those aforementioned App Engine resource limitsâ€”especially when updating or deleting large numbers of items (ie. 1000's to 10000's of items).

[*Pull requests and issue reports on GitHub are welcome!*][impl]

A next step I'd like to take with this thing is to revisit another old friend, the [desktop web app server][desktopserver]. (Also known as the [desktop website][dw].) It seems to me that it would be interesting to scale this server down to a household applianceâ€”say, just for use by my wife and I.

I'd be especially happy if the work I'm doing for a Google-hosted app could be self-hosted at home. Seeing as the development environment for App Engine runs on my laptop, I'm willing to bet I can hack the whole shebang into a simple, special-purpose app to download and double-click on a home desktop PC for use as your sync hub.

Anyway, [check it out][impl] and let me know what you think.

[dw]: http://www.scripting.com/davenet/2001/01/04/desktopWebsites.html#4
[dave]: http://www.scripting.com/davenet/1997/09/14/FractionalHorsepowerHTTPSe.html
[desktopserver]: http://www.decafbad.com/twiki/bin/view/Main/DesktopWebAppServer
[sync-server]: http://hg.mozilla.org/services/sync-server/
[july4]: http://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
[sync]: http://www.mozilla.com/en-US/firefox/sync/
[servers]: https://services.mozilla.com/
