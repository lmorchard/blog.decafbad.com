--- 
wordpress_id: 587
layout: post
title: Feed "Playlists" versus feed:// URLs
excerpt: Feed playlists.  Name it something like `feeds.fss`, and register applications to handle that extension.  Give it a MIME-type, and handle that too.  Sounds just like M3U and PLS files, to me.  Someone tell me why this is a dumb idea.
date: "2005-01-13T12:21:54-05:00"
tags: 
- syndication
wordpress_slug: feed-playlists-versus-feed-urls
wordpress_url: http://www.decafbad.com/blog/?p=587
---
<blockquote>Then, this is the point in the cycle where I remember that the real lesson of the past to learn from is from MP3 playlists, where a link needs to pass one or more URLs to a helper app, and that what we really need is to not to link to our feeds, but to a file that links to them.</blockquote>
<div align="right"><small>Source: <cite><a href="http://kalsey.com/blog/2005/01/handling_rss_in_the_browser/index.html#comment-3236">kalsey.com: Handling RSS in the browser, comment by Phil Ringnalda</a></cite></small></div>

You know, back when [feed autodiscovery][autodiscovery] was first whipped up, I thought that it was great.  Today, there's lots of support for it, and it's even found its way into browsers.  But, well, it still doesn't solve the problem of people clicking on those darn candy-like <img src="http://www.decafbad.com/images/xml.gif" /> buttons.

So, then some folks came up with [a new feed:// protocol for feed URLs][feed].  It seems there's just too much [gone wrong with MIME types][mimewrong] and the like.  When I first heard of feed://, I thought it was a weird and ugly hack, but I never piped up because I was too busy at the time, didn't know much of the details, and was too busy to be bothered to catch up.  Besides, other people were [grousing about it][grouse] already.  And, later, I saw that a slew of aggregators were supporting it, so I figured it must not have been that bad, although I still thought it was odd to kludge around a new URL "protocol" just to pass a feed URL to an aggregator.

But, in the comment above, Phil makes a suggestion that seems ideal to me.  Don't link to feeds directly, don't use a funky protocol, link to a "playlist" of feeds.  URLs linking to MP3 playlists (ie. the [informally specified][winamp] M3U and PLS files) seem to get tossed and handled just fine by your preferred media player.  I don't even know how the MIME-type situation is handled with M3U or PLS links, but it seems to work just fine nonetheless.

And, wasn't there this [Really Simple Discovery][rsd] thing published a long time ago?  Point a weblog management tool at your site, it looks for `rsd.xml`, and it gets all the funky URLs it needs for web services from there?

What if we circled back around with [autodiscovery][autodiscovery] and published a file like this:

    <feeds xmlns="http://www.decafbad.com/2005/01/feeds">
        <link rel="alternate" type="application/rss+xml" title="Full RSS" 
             href="http://www.decafbad.com/index.rdf" />
        <link rel="alternate" type="application/atom+xml" title="Full Atom" 
             href="http://www.decafbad.com/atom.xml" />
        <link rel="alternate" type="application/rss+xml" title="Blog-only RSS" 
             href="http://www.decafbad.com/blog/index.rdf" />
        <link rel="alternate" type="application/atom+xml" title="Blog-only Atom" 
             href="http://www.decafbad.com/blog/atom.xml" />
        <link rel="alternate" type="application/rss+xml" title="Links-only RSS" 
             href="http://www.decafbad.com/links/index.rdf" />
        <link rel="alternate" type="application/atom+xml" title="Links-only Atom" 
             href="http://www.decafbad.com/links/atom.xml" />
    </feeds>
    
Name it something like `feeds.fss`, link your candy-like buttons to it, and register applications to handle that extension.  Give it a MIME-type, and handle that too.  Sounds just like M3U and PLS files, to me.  Someone tell me why this is a dumb idea.

**Update**:  Just to clarify, [before anyone thinks][anyone] I'm just railing against Dave Winer personally--I made a comment below about not liking OPML.  Well, I don't, at least not for this particular purpose.  But, my preferences aside, it's undeniable that most aggregators support OPML import/export in one form or another, so the above example could probably be expressed as OPML with all the same data.

Just one thing, though (and this is part of why I don't like OPML for this):  On my machine, OPML outlines and files with an ".opml" extension open with OmniOutliner.  OPML means "outline" to me, not just "list of feed URLs".  I don't want URLs ending in ".opml" to open in an aggregator.  Can we at least use a different extension and/or MIME type?

[anyone]: http://jaeger.blogmatrix.com/weblog/archives/2005_01.shtml#003186
[rsd]: http://archipelago.phrasewise.com/rsd
[winamp]: http://forums.winamp.com/showthread.php?threadid=65772
[mimewrong]: http://pirate.typepad.com/blog/2003/09/problems_with_m.html
[grouse]: http://alpha-geek.com/2004/09/20/inelegant
[autodiscovery]: http://diveintomark.org/archives/2002/05/30/rss_autodiscovery
[feed]: http://nick.typepad.com/blog/2004/06/feeddemon_and_t.html
