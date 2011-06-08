--- 
wordpress_id: 528
layout: post
title: Info Freako, or who's already past arguing about syndication formats?
excerpt: Where's the state-of-the-art for feed aggregators, and what's next?  I'm tired of reverse-chronological versus three-pane; I'm tired of copying Usenet and email.  What needs to happen next to expand our Info Freako capacity by an order of magnitude or two?  The invention of aggregators has opened the door to the first few orders, but I need more.
tags: 
- syndication
wordpress_slug: info-freako-or-whos-already-past-arguing-about-syndication-formats
wordpress_date: "2004-06-14T18:54:55-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=528
---
> You know that sleep is getting hard to get<br />
> 'Cause you never know what you'll forget<br />
> And I've got to know of all the news<br />
> 'Cause one day there'll be news for me<br />
> <br />
> I never let a headline by<br />
> 'Cause every one will catch my eye<br />
> And though it's tough to keep alert<br />
> You never know what could hurt me<br />

<div class="credit" align="right"><small>Source: <cite><a href=
"http://www.jesusjonesarchive.com/lyrics.htm#Info%20Freako">Jesus Jones, "Info Freako"</a></cite></small></div>

The Syndications Wars are over--at least, as far as I'm concerned.  

It's hard to resist [jumping in][jumping in] where I think someone's got it wrong or when my fingers compel me to feed trolls, but resisting that impulse is what needs to be done.  At this point, all that seems to happen is that the same old threads get recycled.  No one's got anything new to bring, except maybe ad hominem grousing or possibly a Yo Mama joke (though I've yet to see that particular innovation).  Anyone who cares can do a bit of Googling to catch up on the story.

The fact is, I no longer care about RSS versus Atom versus $foo.  Mark Pilgrim enables me to do so with his [feed parser][feedparser], and most other aggregators I might care about have also implemented support for both Atom and RSS.  And if they don't, I can [route around the damage][rss colored glasses] just like I do when I [scrape sites][scrape sites] devoid of any feeds.

While I do prefer Atom over RSS, almost a year later I still say [the magic is in syndication, not the format][syndication magic].  I'll let the tag-level grumblers foam on without comment and just thank them for their work when a good new spec  bubbles up or when something fun and useful comes out.  I'm circling that whole area of concern and sticking a post-it on it that reads: *RSS and Atom both useful, neither perfect, neither going away.*

Whew.  That's a weight off my brain.  Now what is there left to talk about?

Well, how about let's talk some more about what to do with the items we get, once we *do* manage to parse a feed?  (Sheesh, you mean we're not already fighting over that topic?)  

[Rogers Cadenhead wants gluttonous RSS feeders][cadenhead]:

> With thousands of information sources producing RSS and Atom feeds, we need people like Thauvin [whose linkblog is [here][thauvin]] who have integrated weblogging into their daily news-gathering routine. Weblog links are like ant trails -- a lot of people have to link to something good in order to get noticed.

I self-identify as such, since my feed list has topped 550 in count.  But I'm happily surprised to find that I'm not even in the [top 10 of prolific subscribers][prolific subs]--at least I'm not the biggest Info Freako.  (Yet.)  

I'm adding between 2-3 feeds to my list daily, so I can see myself approaching 1000 eventually.  But I'm starting to hesitate at adding one more feed now.  Even with my current streamlined multi-pass skimming process, I'm starting to see diminishing returns.  I breeze past screen loads of chaff that I'll never view, but it still bogs me down.  I can only think that people with twice the subscriptions as I either have more free time, or have a better mousetrap.

The usual response I get toward my subscriptions is, "Why don't you cut that list down to about 100 essentials?"  And even that's said with a smirk, usually by someone with under 50 subscriptions and usually by someone who's not as obsessive an [Info Freako][info freako] as I am.  Thing is, though, good stuff has at one point or another shown up on each and every feed I monitor.  I want to figure out how to scale *up* from 1 to 10 to 100 to 1000 to 10000 sources and beyond.

(Singing interlude: "Info Freako / There is no end to what I want to know")

Besides, this is an area where I can tinker with and learn about another area I'm interested in: machine intelligence and intelligence amplification.  Rogers says, "I want a Bayesian filter that can guess which new headlines I'm most likely to read"  Though someone else might apply Bayes in a way that works for them, I didn't find [my experiments with SpamBayes][bayes] very satisfying.  I suspect it has something to do with the fact that SpamBayes is geared toward sorting out a quasi-binary world of spam-versus-ham, while I'm interested in a spectrum between must-read and shrugs.

But, the idea of introducing another pass through items at the head of the process, this one partially or completely automated, has great appeal.  Done right, this could be the bit that adds an order of magnitude to my capacity to monitor feeds.  I need to investigate other machine learning approaches.

The idea is that, while I freakishly want to catch as much info as possible, I can only handle so much in a day.  For certain, I can't handle everything that might be interesting to me, so I need some prioritization and some pre-filtering before my attention gets applied to the flow.

The way I picture this is trying to apply a sort of [inverted pyramid][inverted pyramid] approach to the incoming flow of items.

I started with a few primitive tools in [AmphetaOutlines' adaptivity to reading patterns][amphetaoutlines], limited mostly to just sorting channels by a count of items read historically.  I also introduced some information hiding and exploration aspects:  I tried to hide or de-emphasize older items by use of font size and weight; and I put items into a JavaScript-driven outline where item descriptions and more ancient items could be hidden or revealed via disclosure triangle.

In my [latest attempt][dbagg2], I've not yet implemented any adaptive sorting, but I've kept and improved the outline display (see: [screenshot #1][dbagg2 screen1], [screenshot #2][dbagg2 screen2]).  Also, I can now mark items as seen and/or flag them to be viewed in a queue for later.  I've got some lame SpamBayes integration in there, but I've let it atrophy in daily use due to a complete lack of usefulness.

I'm starting to think about next steps now toward a more advanced aggregator.  I've still got my [wishlist][wishlist] for AmphetaOutlines, and I've actually covered quite a few of the items with this new aggregator.  But, I'm thinking things like the following would be useful to pursue:

* **What do you think is more important?**  Do you value one group of feeds over another?  Personally, I want to see every single web comic that appears in my queue, most items from [Engadget][engadget] and [Boing Boing][boing boing], and maybe only a few from some of the firehoses I've hooked myself up to.  Also, there are [some][blogger1] [bloggers][blogger2] who post somewhat infrequently, but I don't want to miss a thing when they *do* post.  I need to be able to group and prioritize manually.

* **What do you *demonstrate* as important?**  Which feeds' items receive more of your attention, and within those feeds, what topics and phrases appear most frequently?  The machine should be able to make some observations about your history of behavior and give some input into the organization of items presented.  Also, it should give me some way to give feedback to its recommendations with a simple and lazy thumbs up and thumbs down.

* **Republishing of interesting items to a linkblog is a must.**  On the flip-side, it would be nice to somehow pull in others' linkblogs in a more meaningful way than simply watching their feeds.  I should be able to triangulate some things and get some recommendations based on mutual links predicting future interest in items.  We need to start chasing ant trails unconsciously and automatically.

* **Time-limited subscriptions which expire after a set time, or request renewal from the user.**  Use these to track comment threads which offer RSS feeds.  (Like [this one][comment feed].)

* **More statistics and health monitoring of subscriptions.**  How active are your feeds?  Which are dead &#38; gone, or merely just in hiatus?  Have any moved?

Now, I haven't done any sort of comprehensive survey of the aggregator landscape in a long time, so I'd be very intrigued if any existing software implements these sorts of things.  I've seen some progress toward monitoring feed health, but I've seen next to nothing toward automatic filtering of items and recommendations based on past behavior.  I have seen manually constructed filters, but I'm too lazy to try to figure out how to tell the computer what I want.   I want the machine to ride shotgun, watch and learn.

<a href="http://www.johnny-five.com/"><img src="http://www.johnny-five.com/simplenet/Shortcircuit/Pics/Pictures/Misc/jfive.gif" align="right" alt="Need more input!" hspace="10" /></a> Where's the state-of-the-art for feed aggregators, and what's next?  I'm tired of reverse-chronological versus three-pane; I'm tired of copying Usenet and email.  What needs to happen next to expand our Info Freako capacity by an order of magnitude or two?  The invention of aggregators has opened the door to the first few orders, but I need more.   

Exit singing (while twitching for more info):

> Info Freako, <br />
> There is no end to what I want to know <br />
> <br />
> But it means I'll have the edge over you<br />
> And it means I'll always have the edge over you<br />
> And you know there's nothing that you can do<br />

[jumping in]: http://www.reactuate.com/index.php?itemid=682
[blogger1]: http://interconnected.org/home/
[blogger2]: http://www.ecyrd.com/ButtUgly/Wiki.jsp?page=Main_blogentry_130604_1
[engadget]: http://www.engadget.com/
[boing boing]: http://boingboing.net/
[inverted pyramid]: http://mtsu32.mtsu.edu:11178/171/pyramid.htm
[comment feed]: http://www.pycs.net/system/comments.py?u=0000001&#38;p=1802&#38;format=rss
[wishlist]: http://www.decafbad.com/twiki/bin/view/Main/AmphetaOutlinesWishList
[dbagg2 screen1]: http://www.decafbad.com/2004/06/dbagg2a.jpg
[dbagg2 screen2]: http://www.decafbad.com/2004/06/dbagg2b.jpg
[dbagg2]: http://www.decafbad.com/cvs/dbagg2
[amphetaoutlines]: http://www.decafbad.com/blog/2002/08/05/ooobbf
[bayes]: http://www.decafbad.com/blog/2003/08/16/bayes_agg_one
[info freako]: http://www.jesusjonesarchive.com/lyrics.htm#Info%20Freako "Jesus Jones lyrics"
[thauvin]: http://www.thauvin.net/linkblog/
[prolific subs]: http://feeds.scripting.com/prolificSubscribers
[cadenhead]: http://www.cadenhead.org/workbench/2004/06/10.html#a1802
[syndication magic]: http://www.decafbad.com/blog/2003/07/07/syndications_formats
[scrape sites]: http://www.decafbad.com/twiki/bin/view/Main/XslScraper
[rss colored glasses]: http://www.decafbad.com/blog/2004/05/03/put_on_your_rsscolored_glasses_and_forget_about_atom
[feedparser]: http://diveintomark.org/projects/feed_parser/
