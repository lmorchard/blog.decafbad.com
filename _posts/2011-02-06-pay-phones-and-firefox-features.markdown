--- 
wordpress_id: 2032
layout: post
title: Pay phones and Firefox features
tags: 
- firefox
- browsers
- feeds
- entries
- mozilla
- payphones
- livemarks
wordpress_slug: pay-phones-and-firefox-features
wordpress_date: "2011-02-06T23:32:31-05:00"
wordpress_url: http://decafbad.com/blog/?p=2032
---
**TL;DR**: <em>Pay phones have been disappearing, and so might some Firefox features. But, that's not necessarily a bad thing: Some features steal attention from others that are more important. Some could be spun off into add-ons, which are getting easier to make.</em>

**Update:** <em>Feel free to comment on this blog post. But, if you feel strongly about these features, you might get a better discussion with more people on [this thread from the `mozilla.dev.apps.firefox` newsgroup (in Google Groups)](http://groups.google.com/group/mozilla.dev.apps.firefox/browse_thread/thread/fa6f83e781b962a4).</em>

<p style="display: block; margin: 0 0 1em 1em; float:right;">
<a style="display: block;" href="http://www.flickr.com/photos/thomashawk/4925985819/" title="Phone Don't Work No More by Thomas Hawk, on Flickr"><img src="http://farm5.static.flickr.com/4099/4925985819_9ccbb166f7.jpg" width="333" height="500" alt="Phone Don't Work No More" /></a>
<a href="http://www.flickr.com/photos/thomashawk/4925985819/">Phone Don't Work No More</a> by <a href="http://www.flickr.com/photos/thomashawk/">Thomas Hawk</a>
</p>

When's the last time you used a pay phone? For me, it's been over a decade—which is about how long I've had a cell phone.

As it turns out, [pay phones have been disappearing][pay phones disappear] for awhile now. Why? Because pay phones are expensive to keep in working order. If more and more people have wireless phones, it's less likely that any particular pay phone will result in value for the phone company.

[pay phones disappear]: http://www.nytimes.com/2006/02/19/nyregion/19phones.html?_r=1&pagewanted=print

### So what?

The reason I'm thinking about this is that I'm troubled by a few bugs I ran into in Bugzilla:

* [Remove support for microsummaries](https://bugzilla.mozilla.org/show_bug.cgi?id=622051)
* [Remove smart bookmarks support](https://bugzilla.mozilla.org/show_bug.cgi?id=622045)
* [Remove support for tagging bookmarks](https://bugzilla.mozilla.org/show_bug.cgi?id=622047)
* [Get rid of livemark support](https://bugzilla.mozilla.org/show_bug.cgi?id=622049)

Are these like pay phones? 

Each one requires engineering effort to keep working from release to release in Firefox. Some of them have issues in performance and functionality that could use some attention. And, the introduction of [Firefox Sync][], for example, introduces some new complexities in tracking changes.

[Firefox Sync]: https://services.mozilla.com/

But, do any of these features provide enough value to justify continued attention?

### Microsummaries

Ever heard of [microsummaries][]? I have, and I thought they'd be neat. I installed a plugin on my blog to offer a microsummary, and I tried hacking them into Delicious at one point during a Hack Day. 

That was about 4 years ago, and I haven't thought about them much since. Sounds like a pay phone to me.

[microsummaries]: https://wiki.mozilla.org/Microsummaries

### Smart Bookmarks

I always wondered how those out-of-box "Recently Bookmarked", "Recent Tags", and "Most Visited" folders worked in Firefox. Turns out that you can bookmark [queries against the internal Places database][placesuri] as a persistent search folder. Seems pretty keen.

[placesuri]: https://developer.mozilla.org/en/Places_query_uris

But, I've been using Firefox for years and only just learned about this in the past month. The feature's not very exposed, and it's not obvious how to use it. In fact, [the bug to remove it might list the clearest hints on using it](https://bugzilla.mozilla.org/show_bug.cgi?id=622045#c0).

Seems like it might be a good feature to jettison into an add-on, like a pay phone to play with in your basement.

### Tagging Bookmarks

This is a no-brainer for me: [I like tagging my bookmarks](http://www.amazon.com/gp/product/0470037857?ie=UTF8&tag=0xdecafbad01-20&linkCode=as2&camp=1789&%0D%0Acreative=9325&creativeASIN=0470037857). The problem is that I've exceeded 16,000 bookmarks. It's been years since any browser coped well with my corpus of bookmarks—that's one of the reasons I started really liking Delicious.

However, tagging bookmarks in Firefox is kind of rough. The UI isn't awesome, and the database supporting it could use some work. Rather than improve things, though, [bug 622047](https://bugzilla.mozilla.org/show_bug.cgi?id=622047) proposes removing the functionality altogether.

Here, I'm conflicted: I don't use tags in Firefox, because I don't use bookmarks in Firefox. If they worked better, I might use them. Instead, I use [pinboard.in](http://pinboard.in/u:deusx) or a private Delicious clone of my own that copes with my scale—in fact, I got to this scale because those services handle it. So, usage data from me would support the feature's removal despite what I think I'd like to see.

But, does my *suspicion* that I would use a feature justify someone else's time in making it better? I don't think I can ask for that with a straight face. 

Put another way, I could see how that pay phone they removed from the corner gas station could someday come in handy, but should I expect the phone company to keep it clear of graffiti until I come along with quarters?

### Livemarks

Live Bookmarks (or Livemarks) are bookmark folders whose contents are generated from RSS and Atom feeds periodically polled by Firefox. They're feed subscriptions, built into the browser.

So, when I saw [bug 622049][], my first thought was "**Hey! I'm using those!**" 

I just spent a week building an [add-on powered by Livemarks][fireriver]. I've been using [Fireriver](https://addons.mozilla.org/en-US/firefox/addon/fireriver/) on a daily basis, and I've been thinking about trying more experiments. But, if livemarks are going away, then [I'm working toward a dead end][deadend].

[deadend]: https://bugzilla.mozilla.org/show_bug.cgi?id=622049#c11
[fireriver]: http://decafbad.com/blog/2011/01/27/introducing-fireriver-a-river-of-news-for-firefox-4

Like tagging bookmarks, the UI and feed polling code behind livemarks could use some work. My add-on was an attempt to improve the interface, but I did [report a bug][bug 629742] on performance issues raised by my import of around 700 subscriptions from Google Reader. That's just one more strike against livemarks for [bug 622049][].

[bug 629742]: https://bugzilla.mozilla.org/show_bug.cgi?id=629742
[bug 622049]: https://bugzilla.mozilla.org/show_bug.cgi?id=622049 "Get rid of livemark support"

In the end, if livemarks go away [I'd still have Google Reader][mygr]. I'll have blown a week or so on this add-on, though I did learn some interesting things. And, if Google Reader goes away, [it's not like I've never written a feed reader before][rssbook].

[mygr]: http://www.google.com/reader/shared/l.m.orchard
[rssbook]: http://www.amazon.com/gp/product/0764597582?ie=UTF8&tag=0xdecafbad01-20&linkCode=as2&camp=1789&c%0D%0Areative=9325&creativeASIN=0764597582

Still, this one bothers me the most, in terms of what I want to see for the web itself. [This is better explored in another blog post][browserfeeds], but I want my browser to do more of the surfing for me. I think of bookmarks as long-term relationships to web resources—and livemarks turn those static links into live updates. I can think of a lot of uses for this functionality built into the browser, rather than delegated to [lobster traps][] and content silos.

[browserfeeds]: http://decafbad.com/blog/2011/01/27/what-should-be-done-about-feeds-in-browsers
[lobster traps]: http://ascii.textfiles.com/archives/2848

But, livemarks do complicate things for Firefox engineers. They don't interact well with Sync, and the feed polling code has cases where it can really drag down the whole browser. And, of course, livemarks aren't good for much when a laptop's closed or if Firefox isn't running. Granted, the former happens more often than the latter for me, but we're not talking about an always-on server here in any case.

Are livemarks a pay phone feature? Personally, I don't think so. I think Firefox is diminished if it loses this feature, rather than taking it further.

Although I'm reticent to do so, I might just rebuild livemarks in some form with an add-on if they go away. The good news is that add-ons are getting easier to write, which also deserves its own blog post. The bad news is, I might not have time or motivation to do the work myself. But, either, I'm not all that comfortable clamoring for other people's time for this [beyond registering my disagreement](https://bugzilla.mozilla.org/show_bug.cgi?id=622049#c11) and [backing off](https://bugzilla.mozilla.org/show_bug.cgi?id=622049#c14).

### Conclusion

Most of these things do indeed look like pay phones to me. Most of them seem not to offer enough value to pay for upkeep. 

Livemarks are the exception, in my mind, but I don't have answers as to how to fix their flaws. Maybe they're inherently doomed in the face of ubiquitous computing, maybe they're just in need of a better execution. But, I won't expect other busy engineers to drop what they're doing to come up with those answers in the meantime.

**Update:** <em>Feel free to comment on this blog post. But, if you feel strongly about these features, you might get a better discussion with more people on [this thread from the `mozilla.dev.apps.firefox` newsgroup (in Google Groups)](http://groups.google.com/group/mozilla.dev.apps.firefox/browse_thread/thread/fa6f83e781b962a4).</em>
