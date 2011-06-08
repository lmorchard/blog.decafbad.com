--- 
wordpress_id: 1010
layout: post
title: Microsummaries and Content-Type Mysteries
tags: 
- webdev
- firefox
- microsummaries
- bookmarks
wordpress_slug: microsummaries-and-content-type-mysteries
wordpress_date: "2006-10-29T15:34:49-05:00"
wordpress_url: http://decafbad.com/blog/2006/10/29/microsummaries-and-content-type-mysteries
---
One of my favorite features of the new Firefox are [Microsummaries][ms].  They're like RSS-lite: one-liner summaries of web pages that can be used to keep bookmark titles up to date and get succinct info about a page.  For example, you could get the latest temperature from the title of a weather report bookmark, or the most recent bid price from an auction page.

But, there's one thing that rubs me the wrong way, and it's this:

    <link rel="microsummary" href="microsummary.txt">

That's how you clue a client into finding the microsummary for a given HTML page.  Stick that in your head tag, and you're off.  It's just like [RSS autodiscovery][rd].  Well it is, except for an important detail: What's the Content-Type I should expect at that URL?

You see, microsummaries can be provided as either a direct URL to a plain text summary of the page, or a URL to an XML-based generator providing the means to extract that plain text summary from the page.  But, as spec'ed, you never know which you're going to get until you fetch the URL.  So, when trying to handle a [microsummary][mst], I never know whether to just use the fetched content directly as plain text or whether it's time to fire up the XSL machinery.

I've seen some sites toss in a type="text/plain" or type="application/xml" attribute - which is very helpful and what I really want to see - but it's not in [the spec][mst].  From a cursory perusal of Firefox source code, it looks like the browser tries to sniff the Content-Type header returned by the web server - but that sucks, because web servers often lie or are confused about Content-Type.  I need to read more into that source code, so I can at least do as well as Firefox does.

Eh, it's a small gripe, but one on which I've spent too much time already.

[rd]: http://diveintomark.org/archives/2002/05/30/rss_autodiscovery
[ms]: http://microsummaries.org/
[mst]: http://wiki.mozilla.org/Microsummaries
