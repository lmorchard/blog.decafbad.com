--- 
wordpress_id: 1011
layout: post
title: Event Delegation based DHTML Drag and Drop?
wordpress_url: http://decafbad.com/blog/2006/10/31/event-delegation-based-dhtml-drag-and-drop
---
So, as the urge to tinker rises again, I've started playing with [YUI][] and cracked open some [XoxoOutliner][] code again.  One of the things that struck me like a bolt from the blue recently is the notion of [event delegation][ed].  For the most part, I've treated event bubbling as a nuisance, except for where it came in handy in keyboard input handling.  But avoiding the need to individually track events on every list element on the page via instantiated objects and methods is *hot* and *forehead-slappingly obvious* once you've seen it working.  Just implement one set of event handlers on the outline root element (ie. UL or OL), and do the right thing as events come in from the list child elements.

Thus, while I can do outline node expand/collapse with ease, my goal is to implement an [event delegation][ed] based approach to dragging outline nodes around.  Apropos of that, I've been poking at [how event delegation it works in YUI][edy].  While there's nothing much special about it in general, I've run into a bit of a snag when it comes to drag-and-drop.

See, YUI comes with a [rather nice drag-and-drop abstraction][yuidd] that I'd like to use.  That abstraction, however, requires the instantiation of lots of little objects - one per outline node.  Definitely not delegation-based: The problem is that I'll be adding and removing outline nodes at whim throughout the lifetime of the page, which would require lots of care to ensure that I'm maintaining drag-and-drop wrapper objects.  I've done that a bit in [XoxoOutliner][]; it sucks.

So, I was able to build part of a delegation-based drag tracker from scratch.  I'm sad to lose the other niceties that the YUI DnD offers, but it works.  The problem now, though, is the *drop* part of the equation.  I can drag elements around the page until my heart's content, but I can never quite tell in what context I've dropped it.

I poured through the source code for the YUI DnD implementation, as well as the implementation of a few other JS frameworks' DnD offerings.  The general solution seems to be calculating and caching the page coordinate regions for each element relevant in the drop operation.  In my case, that usually includes every outline node on the page.  That's easy when you have lots of little objects instantiated - you just iterate through them and match up regions with the coordinates where the drag stopped.  But, part of my win with event delegation was that I don't have to maintain a pile of objects.

Oh yeah, and did I mention that I don't assign IDs to all the little list items making up my outline?  And that I don't particularly feel like doing so?  That also throws a monkey wrench in the YUI DnD paradigm.

The only idea I have so far is that I need to at least build a cache mapping regions to outline nodes, and keep it fairly well maintained.  That should be lighterweight than a fleet of DOM event wrappers, but still annoying.  I could trigger a cache refresh when a drag first starts, but that will probably drag down UI response.  I could trigger it whenever the outline changes, but that's just moving the burden.  And then, who knows how I'll map ID-less elements to their respective regions, while ensuring I stay clear of memory leaks.  That's still semi-voodoo to me, and I feel ashamed of that.

Eh, maybe it won't be as bad as I think.  But, to anyone who understands what I just spewed:  Any ideas?

[yui]: http://developer.yahoo.com/yui/
[xoxooutliner]: http://decafbad.com/trac/wiki/XoxoOutliner
[ed]: http://icant.co.uk/sandbox/eventdelegation/
[edy]: http://yuiblog.com/sandbox/yui/v0114/examples/event/delegation.php
[yuidd]: http://developer.yahoo.com/yui/dragdrop/
