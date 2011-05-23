--- 
wordpress_id: 2022
layout: post
title: What should be done about feeds in browsers?
wordpress_url: http://decafbad.com/blog/?p=2022
---
**TL;DR**: <em>Browsers need help doing a better job using feeds for discovery, aggregation, and publishing on the web to keep us from swimming into self-destructing lobster traps.</em>

Last week, I wrote [some blog posts](http://decafbad.com/blog/tag/bug578967) about [Bug 578967](https://bugzilla.mozilla.org/show_bug.cgi?id=578967), wherein the feed auto-discovery icon in [Firefox 4](http://www.mozilla.com/en-US/firefox/beta/) has been moved off the URL bar and hidden by default. I support that decision of [the UX team](http://planet.firefox.com/ux/), because [that feed button is a slacker](https://heatmap.mozillalabs.com/). And even if it does get used, [I'm not a fan of what it does anyway](http://decafbad.com/blog/2011/01/15/what-happened-to-feed-autodiscovery-in-firefox-4#serving).

But, I've got lots more rattling around in my head about this stuff.

### What's the point of feeds?

Feedsâ€”that's RSS and Atom and maybe even JSONâ€”let robots pull lots of stuff from a bunch of places and pile it all together in one spot for your perusal, analysis, and remixing pleasure. Feed readers and news aggregators do the surfing for you, so you don't have to.

But, Twitter and Facebook and others have managed to make *the people themselves* all gather in one spot. So, to see what those people are saying and doing, you just have to go *there*â€”kind of like what feeds promised, right? Only, you go *there* rather than all that stuff coming *here*.

The problem is, even if the logo says it [loves you](http://www.flickr.com/photos/dunstan/524137648/), the people who made it say that [won't always stay in charge](http://www.flickr.com/help/forum/en-us/107408/). And, someday, when whomever's left rides off into the [sunset](http://techcrunch.com/2010/12/16/is-yahoo-shutting-down-del-icio-us/), you'll learn how much [they didn't care about you](http://archiveteam.org/index.php?title=Why_Back_Up%3F) in the end.

<p style="text-align: center"><a href="http://www.flickr.com/photos/herzogbr/2261662706/" title="Flickr Loves You by herzogbr, on Flickr"><img src="http://farm3.static.flickr.com/2003/2261662706_db086ea4bb_m.jpg" width="" height="64" alt="Flickr Loves You" /></a> <strong style="font-size: 200%; padding: 0.5em;">vs</strong> <a href="http://www.flickr.com/help/forum/en-us/107408/"><img src="http://l.yimg.com/g/images/en-us/flickr-yahoo-logo.png" height="50" style="padding: 7px; background: #fff"></a></p>

For some people and some places, that's no big tragedy. It's just a party; you go home when it's over. You made memories, you hope to find some of those people again elsewhere. [Pownce croaked](http://blog.pownce.com/2008/12/01/goodbye-pownce-hello-six-apart/), and [so did Vox](http://www.wired.com/epicenter/2010/09/six-apart-shuts-down-vox/), but who cares? There's always Twitter next door for the afterparty.

But, what if a world you lived in [evaporated while you were on vacation elsewhere for the holidays](http://ascii.textfiles.com/archives/2444)? I guess you could say that was just a game and, again, who cares?

What if [Flickr](http://www.flickr.com/) went away just like that? People are not only partying thereâ€”they're leaving their visual memories at the coat check. Things are a little more real there, by some definitions thereof.

What if you never swam into that [lobster trap](http://ascii.textfiles.com/archives/2848), though? What if your words and images and creations were borrowed and copied, but never wholly kept in someone else's bucket? What if [Flickr](http://www.flickr.com/) were just like [Google Search](http://google.com)? That is, a collector and an indexâ€”but never the hostâ€”of photos and conversations?

Feeds can help make that happen, but not by themselves.

### Do feeds belong in the browser?

Well, yeah. Would sites like Twitter and Facebook have been as successful if feeds worked better in the browser? I think so. But, by working better, I don't just mean improvements to that funky blue thing that showed up in the location bar every now and then. No, I mean all of the following:

* **Discovery** â€” help me find and follow interesting people and things
* **Aggregation** â€” give me one spot where what I find and follow is delivered to me
* **Publishing** â€” enable me to post things where people (and their agents) can find and follow

To me, this is where Twitter and Facebook are totally nailing it. But, much of this can happen in the browser, and I think more of it should. Projects like [RockMelt](http://www.rockmelt.com/) and [Flock](http://www.flock.com/) have seemed promising to me in this context, but have yet to really thrill me. I don't think they go far enough.

There is a point where the rubber (client) meets the road (server)â€”but that point can live [so much farther down the stack than it does now](http://scripting.com/stories/2011/01/11/howToShareABucketOnS3.html). Mind you, I don't want a revival of [Netscape Gold](http://www.zisman.ca/netgold/) as suchâ€”but recall that ["the first browser was an editor, it was a writer as well as a reader"](http://news.bbc.co.uk/2/hi/technology/4132752.stm).

We need some services and hosts out there as rendezvous points for our browsers and agents, but we really don't need any of those services to collapse into [the next all-encompassing AOL-style singularity](http://buddycloud.com/cms/content/we-are-aol-days-social-networking). There's money to be made there, but most of us are the product.

### Whose job is it anyway?

I'd like to see my employer, Mozilla, do more with feeds in the browserâ€”and I suspect we will. [Mozilla Labs has had some interesting Concept Series topics](http://mozillalabs.com/blog/2010/03/online-identity-concept-series/), and I look forward to seeing some of those things get pursued further. If I can carve out the time, I wouldn't mind helping.

Something I find interesting about feed auto-discoveryâ€”the thing that started this latest round of buzzâ€”is that it didn't originate with browser makers. [RSS auto-discovery](http://diveintomark.org/archives/2002/05/30/rss_autodiscovery) was itself discovered [by bloggers](http://decafbad.com/blog/2002/05/31/oooago), way back in 2002. It wasn't until we sussed out the details of that [HTML link tag](http://www.w3.org/TR/REC-html40/types.html#type-links) and shoved it into our pages that browsers like Firefox started looking for it.

Hell, even though [RSS started with Netscape](http://en.wikipedia.org/wiki/Rss#History), it took [Dave Winer and UserLand and friends running with it](http://scripting.com/davenet/2000/09/02/whatToDoAboutRss.html) to keep it alive and kicking. Now, Dave's [suggested forking an open source browser](http://scripting.com/stories/2011/01/11/krocCamenProvesRssIsVeryMu.html) to show Mozilla how it's done. I support the sentiment, but there are easier ways to go about this.

### Making it your job

[Christopher Blizzard](http://camendesign.com/rss_a_reply):
<blockquote>We created add-ons with the original Firefox as a way to be able to say â€œnoâ€ in a constructive manner. If you want something that you think is important to you, you can make an add-on.</blockquote>

That could be taken as a cop-out, but it's not. With the efforts behind [Jetpack](https://jetpack.mozillalabs.com/)â€”now just *the* [Add-on SDK](http://blog.mozilla.com/addons/2010/12/09/announcing-add-on-sdk-1-0b1/)â€”building add-ons for Firefox is being made easier. Rather than dealing with a morass of XUL and obscure APIs that I know has scared me personally away all these years, you can now do most everything you'd like though [much-simplified JavaScript APIs](https://jetpack.mozillalabs.com/sdk/1.0b1/docs/#package/addon-kit) and HTML/CSS.

In other words, if you are a web developerâ€”albeit a fairly advanced oneâ€”you can make an add-on for Firefox. Hopefully, as the Add-on SDK advances, the bar to participation will continue to drop.

### To be continued

I'm running out of steam and it's time for bed, so I think I'll just trail off for now. I do have a bit more in me, though. The next thing is about taking my own advice in that last section and making some of this *my* job to fix.
