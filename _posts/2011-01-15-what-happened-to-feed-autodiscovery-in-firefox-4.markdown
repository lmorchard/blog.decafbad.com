--- 
wordpress_id: 1976
layout: post
title: What happened to feed auto-discovery in Firefox 4?
wordpress_url: http://decafbad.com/blog/?p=1976
---
**TL;DR**: <em>The feed button is not dead; it's just been sent to sing backup in Firefox 4 because it's not pulling its weight. This post talks about why things have changed.</em>

There's [a brouhaha](http://camendesign.com/rss_a_reply) about [Bug 578967](https://bugzilla.mozilla.org/show_bug.cgi?id=578967), wherein the feed auto-discover icon in [the Firefox 4 Beta](http://www.mozilla.com/en-US/firefox/beta/) has been hidden by default. Being a feed nerd, the author of a book on the stuff, *and* a Mozilla employee—I've got at least a few opinions.

This post is one of [several on this subject](http://decafbad.com/blog/tag/bug578967).

### Defaults are hard to pare down

The [feed icon still lives](http://decafbad.com/blog/2011/01/15/how-to-use-feed-auto-discovery-in-firefox-4) in [the Firefox 4 Beta](http://www.mozilla.com/en-US/firefox/beta/); it's just not there by default any more. But, if you look at the controls available in [the toolbar customization panel](http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-01.png), you'll notice a *lot* of things that don't show up by default—there are a lot of things in there, period.

This is the dilemma for [the Firefox User Experience team at Mozilla](http://planet.firefox.com/ux/): Like it or not, one of the main themes of this next generation of browsers is minimalism—faster, smaller, less browser to get in the way of what you're browsing. Yet, at the same time, Firefox 4 has the features of Firefox 3.6 and more.

You can't just cram it all in there, so what gets prime real estate by default? People say it's just a few pixels, that feed button—but is it so much more important than anything else that could go there? And before you answer, consider that not just for your personal use, but for the 100's of millions of people using Firefox. How do you check your own biases and make a decision on that scale? You could make an educated guess, make a gut check. A lot of brilliant design happens that way.

You can also [gather some telemetry from beta installs to see what people really use](https://heatmap.mozillalabs.com/). Looking at a heatmap of clicks, the feed button is an absolute stinker. This isn't a random whim of the UX team—seriously, it's an **order of magnitude** less used than anything else in the toolbar (notice the one black spot):

[<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/heatmap.png" alt="heatmap.png" border="0" width="600" height="75" />](https://heatmap.mozillalabs.com/)

There have been comments dismissing the validity of that heatmap study. But, as far as I can tell, none of them really stick. So, for the sake of argument and a shorter blog post, let's assume barely anyone is using the feed icon and that it's not pulling its weight in this new age of browser minimalism.

Keep in mind that Firefox isn't the only browser to deprioritize the feed button: *Google Chrome doesn't even have a feed button at all*, and for many people that's the gold standard for minimal browser UI:

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-chrome.png" alt="feed-sub-chrome.png" border="0" width="600" height="242" />

<a name="serving"></a>
### Serving the users

Let's hammer on the point of disuse some more—what's the payoff for clicking that thing, anyway?

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-styling.png" alt="feed-sub-styling.png" border="0" width="600" height="424" />

* +1 — You get an option to create a [Live Bookmark](http://www.mozilla.com/en-US/firefox/livebookmarks.html), which is really handy for things like Bugzilla searches or light headline reading. (I like those so much that I tried building them on the server at Delicious once, but we never quite worked it out at scale.)

* 0 — You get a list of sites to which Firefox will delegate subscription, if you happen to have [installed a content handler](https://developer.mozilla.org/En/DOM:window.navigator.registerContentHandler). Useful if you know what it's about; a mystery if you don't—not much more useful than a bookmarklet, to me.

* -1 — You get a plainly-styled version of what you were probably already looking at on a site, [something I criticized back in 2006](http://decafbad.com/blog/2006/11/02/firefox-20-breaks-client-side-xsl-for-rss-and-atom-feeds), like some are criticizing the feed icon change now.  (At the time, I was working for [a marketing company](http://organic.com), and the change cost me days trying to incorporate branding in feeds on [a client's site](http://www.jeep.com/en/autoshow/feeds/jeep-all.xml). I think we gave up after a bit, but I suspect that [FeedBurner](http://feedburner.com) built a nice business routing around that change.)

That's been status quo for years, and it's less than compelling—I've even had people ask me if they broke the page when the button was clicked on accident.

So, given little reward for clicking that feed icon, *pushing it into the background in **its current state** is a service to the users of Firefox*. In other words, that feed button has to get a lot more interesting if it's going to serve alongside UI all-stars like **Back**, **Reload**, and **Location**. 

Hell, even with Firebug installed, I use **View Source** more than the feed button these days, and I've never stuck *that* on the toolbar.

### Leading the web

The most compelling response I've seen to the "removal" of the feed auto-discovery button is the challenge that Mozilla and other browser makers should be *improving* feed-related features, rather than pushing them into the background. With this, I wholeheartedly agree—but I'm not entirely sure what to do about it.

So, there's a balance here: Make the **experience of the web better** by improving how Firefox handles what's already out there, and **make the web itself better** by building more powerful and enabling technologies into Firefox and other products. In the best of times, Mozilla can do and has done both at once. [WebGL](http://en.wikipedia.org/wiki/WebGL) and technologies associated with HTML5 represent great examples of this.

But, alas, syndication feeds in the browser have stagnated. The feed button has been a weak feature *for years*. In the meantime, other things have taken priority in the Firefox project. The rise of Twitter and Facebook and more complex applications on the web have reduced the need for most people to interact directly with feeds, so demands for attention to the feed button haven't exactly topped the charts in comparison to things like [making sure Flash doesn't crash the browser](https://support.mozilla.com/en-US/kb/The%20Adobe%20Flash%20plugin%20has%20crashed) and [getting super fast](http://arewefastyet.com/) for everything else. 

### Ship it!

In the end, Mozilla has a browser to ship. The decision on the feed button *has been made* and, believe it or not, with a great deal of thought behind it. 

I know that this is the first time many people have heard of this change, but many already have heard and have given the UX team a number of earsful. Coming in at this late stage and requesting—nay **demanding**—a reversal of that decision will do nothing but piss off all the people who've been banging away at this and many other things up to now. They're people who've worked hard, stayed up late—and the last thing anyone wants to do is rehash every conversation ever about the topic.
