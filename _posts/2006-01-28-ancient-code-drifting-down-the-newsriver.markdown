--- 
wordpress_id: 842
layout: post
title: Ancient code drifting down the newsRiver
wordpress_url: http://decafbad.com/blog/?p=842
---
So, while working through some writing blockages last weekend, I started doing [some hacking][hack] on [Dave Winer's newsRiver][new] running on the [OPML Editor][opml] platform.  (Oh, and it *is* a platform, maybe more so than even emacsâ€”don't let the moniker 'editor' fool you.)

Here's the thing:  It was a lot of addictive fun, and it takes me back to the [love/hate thing I had with Radio][lh], back toward the first days of this blog.  This Frontier / Radio / OPML Editor environment is undeniably satisfying for me to work in.  It's like potato chips:  Jump to an outline here, tweak some code there, mangle an outline node up there, reload a browser page, watch things goâ€”lots of moments of instant gratification all building incrementally atop one another.

In one packageâ€”which reminds me a lot of [Squeak][]â€”the [OPML Editor][opml] bundles a crazy amount of integrated machinery for both Windows and Mac OS X:

* UserTalk, a very capable scripting language
* An IDE based on outlining, somewhat like Python's syntactic indentation
* Persistent on-disk hierarchical hashtables (aka the Object Database)
* Code and data all live in the same object database
* A web server and a host of other networking codeâ€”including Jabber messaging, although I can't attest to its freshness.
* Blog editing and no-effort external web hosting file synch
* [Hot patching][hp] and easy upgrades that most other software packages dream of
* Years and years and years of (mostly) working code with datestamped change notes and living history.

And the thing is?  This was the state of the art for Radio back in 2002â€”and earlier than that even for Frontier.  Fast forward from then till today, and you'll find that [Frontier is now Open Source][fso]â€”with many of the same sorts of warts Mozilla's open source release helpfully revealed back in 1997.  (Some hero needs to come along and port this beast to Linux!  Good luck!)  And now, much of the guts of Radio are released as the [OPML Editor][opml].  

In a lot of ways, this whole family of apps built on this common ancestry of code is [really shitty software][shitty].  Kind of like [all that code on the *Qeng Ho* from Vernor Vinge's *A Deepness in the Sky*][code].  This stuff crashes and sets itself on fire a lot, but then again it's amazing to see just how many wheels have been reinvented and re-reinvented since 2002 (and before) when I fire up this code today.

And now, it looks like the embers are stirring for this thing again.  There's been a lot of time for a lot of angst to fade from a lot of places, and it looks like there's a new crop of fresh people rediscovering this stuff.  

So, anyway, I like these potato chips.  I think I want to start munching on them again, as time permits.  Oh, and while I'm talking about potato chipsâ€”I have to say, [don't pee in the potato chips][pee] and be nice to the guy holding the bag.

<!-- tags: winer rss syndication radio usertalk frontier vinge opml -->

[pee]: http://decafbad.com/blog/2006/01/28/dont-pee-in-the-potato-chips
[squeak]: http://www.squeak.org/
[code]: http://decafbad.com/blog/2005/02/24/ancient-software-and-programmer-archaeologists
[shitty]: http://davenet.scripting.com/1995/09/03/wemakeshittysoftware
[hp]: http://decafbad.com/blog/2002/04/26/oooabf
[fso]: http://frontierkernel.sourceforge.net/
[lh]: http://decafbad.com/blog/2002/04/11/ooooho
[opml]: http://support.opml.org/
[new]: http://scripting.wordpress.com/2005/12/29/why-im-working-on-an-aggregator/
[hack]: http://decafbad.com/blog/2006/01/21/a-bit-of-newsriver-hackery
