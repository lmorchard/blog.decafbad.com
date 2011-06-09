--- 
wordpress_id: 1031
layout: post
title: Vienna is now my weapon of choice for feeds
date: "2007-01-02T16:37:48-05:00"
tags: 
- metablogging
- webdev
- aggregators
- rss
- software
- osx
wordpress_slug: vienna-is-now-my-weapon-of-choice-for-feeds
wordpress_url: http://decafbad.com/blog/2007/01/02/vienna-is-now-my-weapon-of-choice-for-feeds
---
In the last few days, I've switched news aggregators again - this time to [Vienna][].

I've got a [long][l1], [long][l2], [long][l3] [history][l4] of doing this - partially because of my [serial enthusiasm][se], and partially because none of the aggregators I've used so far have satisfied all of my itches.  Some tie up my laptop in terms of memory and CPU, some aren't fast enough UI-wise to help me really blaze through skimming, and some aren't flexible enough for me to tweak to my particular liking.

At this point, though, [Vienna][] comes really close to what I've been wanting for years.  It's open source ([check it out!][vsvn]); uses WebKit to offer a [theme-able][vt] feed item display ([hello Colloquy!][wk]); and uses SQLite 3 for persistence ([with schema documentation!][vdb]).  Out of the box, it's a pretty nice app, but it was even nicer when I started poking under the hood.  I've even [submitted my first small patch][vpatch], which got accepted into the codebase.

When last I tried [Vienna][], it was on my poor old PowerBook G4 12" 867Mhz and it was a somewhat rough and bad tasting experience.  At the time, [NetNewsWire][] was my tool of choice, and [Vienna][] was lacking some features - like, say, a user-sortable list of subscription folders and feeds.  It also thrashed a lot and generally made me Force Quit it and move on.  But now, on my new-ish MacBook Pro, the performance is stellar with my set of 500+ feeds and my few showstopper missing features are no longer missing.  

Now, it seems like [NetNewsWire][] is the app that thrashes for me and gets a Force Quit.  I need to try [NNW][NetNewsWire] a bit more and figure out if it's just my initial import of subscriptions that drags things down - but [Vienna][]'s got me now.  It's catching up mightily fast with the feature list of NNW.  And, nothing beats open source software for tossing in a few tweaks to things that are just *not quite* doing what I'd like.

Again, since I'm a [serial enthusiast][se], I have no idea if I'll be a regular contributor of patches to [Vienna][] or even offer any commitment to the project - but I'm definitely happy with it at the moment.

[vpatch]: http://sourceforge.net/mailarchive/forum.php?thread_id=31310885&forum_id=48723
[vt]: http://www.opencommunity.co.uk/vienna_styles.php
[vsvn]: http://vienna-rss.svn.sourceforge.net/svnroot/vienna-rss/trunk/2.1.0/
[vdb]: http://vienna-rss.sourceforge.net/public/DatabaseSchema.pdf
[wk]: http://decafbad.com/blog/2004/02/12/colloquy-irc
[Vienna]: http://www.opencommunity.co.uk/vienna2.php
[NetNewsWire]: http://www.newsgator.com/NGOLProduct.aspx?ProdID=NetNewsWire
[l1]: http://decafbad.com/blog/2006/08/18/good-gregarius
[l2]: http://decafbad.com/blog/2006/02/12/further-work-on-decafbadnewsriver
[l3]: http://decafbad.com/blog/2005/10/05/feedspool-is-progressing-nicely
[l4]: http://decafbad.com/blog/2004/08/05/introducing-dbagg3-an-atom-powered-clientserver-aggregator
[se]: http://decafbad.com/blog/2006/05/26/confessions-of-a-serial-enthusiast
