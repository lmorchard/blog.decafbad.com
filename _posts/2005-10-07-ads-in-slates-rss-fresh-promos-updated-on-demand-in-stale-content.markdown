--- 
wordpress_id: 722
layout: post
title: "Ads in Slate's RSS: Fresh promos, updated on demand in stale content"
tags: 
- asides
wordpress_slug: ads-in-slates-rss-fresh-promos-updated-on-demand-in-stale-content
wordpress_date: "2005-10-07T10:42:38-04:00"
wordpress_url: http://decafbad.com/blog/?p=722
---
Damn you, Slate.  I'm really starting to get annoyed with various sites' implementation of advertising in feeds.  Yes, [I'm looking at *you* too, Boing Boing][bb].  

The one upside to the ads in Boing Boing's feed, so far anyway, is that at least they don't change from poll-to-poll.  So, although I get a face full of the ads repeated down my aggregator page, at least I only see them each once.

With [Slate's feed][sl], on the other hand, entries I've already fetched change on every poll to the feed because they randomly rotate through and generate new ads every time I request the feed.  So, in effect, nearly every entry in the feed ends up being "updated" when I request it.

**This sucks.  Please stop.  Stop now.  Feed entries are not the same as web pages.**

Of course, part of this has to do with [FeedSpool][fs]'s approach to tracking whether an entry is new or has changed.  That is, it takes an MD5 hash of the entry's XML source and uses that as a unique ID.  Yes, this is lazy.  But it's worked for me for a few years now in my other aggregators.

What I really should be doing in [miniagg][ma] is watching the unique IDs on entries to determine freshness, when they're available.  Which, thankfully, they are in Slate's feed.  In other feeds, well, I'm not always so lucky, which is how the MD5 technique came about in the first place.

Nothing's ever nice & easy, is it?  :)

[bb]: http://archive.scripting.com/2005/09/20#whenRssIsntVeryGreat
[fs]: http://decafbad.com/trac/wiki/FeedSpool
[ma]: http://decafbad.com/trac/browser/trunk/feedspool/plugins/miniagg
[sl]: http://slate.msn.com/rss/
