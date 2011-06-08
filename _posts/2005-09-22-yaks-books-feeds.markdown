--- 
wordpress_id: 681
layout: post
title: Yak shaving, book pimping, and feed spooling
tags: 
- metablogging
- syndication
- gaming
- writing
- feeds
- thebook
- yaks
wordpress_slug: yaks-books-feeds
wordpress_date: "2005-09-22T16:31:16-04:00"
wordpress_url: http://decafbad.com/blog/?p=681
---
Well, of course I've lapsed pretty much right back into silence after [having shaken this place up][redesign] and [having announced the arrival of the book][book].

The culprit, of course, is [yak shaving][yak].  Again.  True, life itself has been pretty busy lately.  The days are booked, the weekends have been filling up--and in spare moments I've been obsessed with [jumping from building to building][hulk].  But, when it comes down to me and a pile of code on the screen, I find myself in ever further depths of recursion.

For instance, I keep meaning to get down to posting some [lightweight "asides"][asides] in place of my old ["quick bullets"][quick] posts I was doing.  But, of course, before I do that, I want to do some [Kottkesque template mungeing][kottke] to more properly present these smaller bits.  

And, though I'm actually most of the way done making another rev to the theme here, I also want to fold my linkblog back into the site.  The absence of these [has already been noticed][noticed], so I'd like to give those a proper treatment.

In addition, I still mean to start pimping my new book a bit; maybe even starting tonight.  I've got a notion to post teasers highlighting a few of my favorite things.  And then, of course, there's the [neglected companion site][hackingfeeds] on which I've yet to spend much time at all.  But I've got grand plans, including some which go beyond the book itself and toward making [hackingfeeds.com][hackingfeeds] a regularly updated and relevant resource.

Speaking of that...  I've also continued working a bit with some feed hacks since finishing the book.  

[FeedSpool][feedspool] is one of these: I've revived some of FeedReactor's old code--this time aiming for a much higher degree of simplicity, trying to stick with standard Python modules, and dumping the database altogether.  

I've been meaning to make a more formal announcement about this thing, once it's a bit more in usable shape.  In a nutshell:  It polls feeds and downloads the data.  New entries are split out into individual files, like an email or usenet spool.  That's it.  Other programs are expected to do the clever bits.

And, to go along with [FeedSpool][feedspool], I've been toying with building a Spotlight importer for OS X Tiger which indexes RSS and Atom feeds and entries.  Not in Subversion yet, and not nearly ready for public consumption, but it's been pretty fun to play with.  (And I totally forgot just how many feeds I have lying around on my hard drive!)

Anyway, that's enough for now.  Time to post this and get to thinking about what I want to post next!

[feedspool]: http://decafbad.com/svn/trunk/feedspool/
[quick]: http://decafbad.com/blog/2005/08/12/quick-and-random-thoughts
[noticed]: http://decafbad.com/blog/2005/09/12/redesigninprogress#comment-1850
[kottke]: http://www.kottke.org/03/11/kottke-redesign
[asides]: http://codex.wordpress.org/Adding_Asides
[hackingfeeds]: http://www.hackingfeeds.com/blog/
[book]: http://decafbad.com/blog/2005/09/13/hacking-rss-and-atom-is-out "Hacking RSS and Atom is out! » Archive » Blog » 0xDECAFBAD"
[redesign]: http://decafbad.com/blog/2005/09/12/redesigninprogress "Redesign in progress (or, no need to adjust your set) » Archive » Blog » 0xDECAFBAD"
[yak]: http://www.catb.org/~esr/jargon/html/Y/yak-shaving.html "yak shaving"
[hulk]: http://www.hulkgames.com/us/ "THE INCREDIBLE HULK: ULTIMATE DESTRUCTION"
