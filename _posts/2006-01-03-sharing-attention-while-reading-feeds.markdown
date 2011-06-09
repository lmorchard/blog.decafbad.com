--- 
wordpress_id: 814
layout: post
title: Sharing attention while reading feeds
date: "2006-01-03T09:45:01-05:00"
tags: 
- aggregators
- rss
- syndication
- atom
- attention
wordpress_slug: sharing-attention-while-reading-feeds
wordpress_url: http://decafbad.com/blog/?p=814
---
<blockquote cite="http://blogs.zdnet.com/SAAS/?p=82">Instead of reading their individual selections of RSS feeds privately, everyone should be encouraged to publish those aggregated feeds on the Web. ... the simple act of publishing those aggregations then makes them available to others, and thus makes them amenable to network effects in a way that they never can be if they're kept private.</blockquote>
<small style="text-align:right; display:block">Source: <a href="http://blogs.zdnet.com/SAAS/?p=82">» It's time to bury RSS | Software as services | ZDNet.com</a></small>

My current two responses to the above:

* I love my [popular links][pl] summary feed.
* [Attention.xml][att] is starting to make sense to me.

Putting these two together could be a very powerful tool for bringing network effects to feed reading.

First off, one of the most useful feeds I have is my private Popular Links feed.  [Touting my book again][book], I showcase the [script behind this thing][pl] in Chapter 15.  I've had this running for well over a year, and it's always my first stop in the feed reader.  Almost without fail, this tends to surface what's buzzworthy.

Basically, this script scans all the current entries of all my subscribed feeds for unique hyperlink URLs found in descriptions and summaries.  It collates all entries by these links, then sorts by the number of entries under each link.  A threshold is applied, filtering for links pointed to by 3 or more entries.  

At the end, I see a new feed entry displaying the most linked-to things of the moment.  Think of this as a kind of real-time PageRank.  How's that for network effects?

I think this is *sort of* how [Memeorandum][meme] works, only this is constrained to the feeds in my subscription list.  I've been considering making this script a full-on service:  Upload an OPML export from your aggregator, get your own Popular Links feed.  I've got all the parts laying around but I haven't yet had time to put them together—**but if it sounds like something useful, and possibly worth clicking a Paypal donation button, let me know!**

Secondly:  [Attention.xml][att] makes a lot of sense with regard to the above-quoted article.  When I first heard about [Attention.xml][att], I merely cocked my head at it and made a confused sound.  This was before I caught the microformats bug, and before I realized that I [started reinventing it][blogroll] a bit in my own ramblings.

Basically, [Attention.xml][att] is a feedroll enriched with data about the entries you've lately read from each feed.  It's in an XHTML-based format which—albeit ugly in my opinion and in need of more elegant microformat influence—is indeed viewable in a browser.  In a sense, this format is an auto-blog of my feed consumption.  I was looking for hacks for my NetNewsWire in AppleScript, when I found [this Attention.xml generator][gen].  Seeing the output of that, it all clicked.

Combining [Attention.xml][att] with my Popular Links algorithm could be a very powerful thing, methinks.  Rather than waiting for my friends to tip over the laziness point to blogging about something, I could digest their shared [Attention.xml][att] files and collate the links they've merely *read*.  In this way, I could build an *AttentionRank* for various things, and cause the cream to rise to the top in my feed reader.

I'm pretty sure that I'm playing catch-up here, but this all suddenly seems hot to me.  And not to mention, it seems neat that I have all the pieces laying around to build it.  The only bad thing is that I just don't have the time to spare—I've already spent too much time writing this blog post!

Anyway, maybe you'll hear more from me about this soon.

[gen]: http://decafbad.com/blog/2005/12/01/blogrolls-grow-up-to-become-feedrolls
[blogroll]: http://decafbad.com/blog/2005/12/01/blogrolls-grow-up-to-become-feedrolls
[att]: http://tantek.com/presentations/2005/01/attentionxml.html
[meme]: http://memeorandum.com/
[pl]: http://decafbad.com/trac/browser/trunk/hacking_rss_and_atom/ch15_popular_links.py
[book]: http://www.amazon.com/exec/obidos/ASIN/0764597582/0xdecafbad01-20?creative=327641&camp=14573&link_code=as1
