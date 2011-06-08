--- 
wordpress_id: 641
layout: post
title: The right place for data in your feed
wordpress_slug: the-right-place-for-data-in-your-feed
wordpress_date: "2005-05-05T11:08:42-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=641
---
I've suddenly gotten very interested in [microformats][mf], especially since it struck me very soundly that they belong in this final chapter of my book about extending feeds.  

I started off writing a bit about [`mod_event`][me] and [RVW][rvw] with respect to extending feed formats with additional metadata, but then the [microformat][mf] thing hit me:  Why extend the feed format metadata when you can extend the feed content?  This seems so obvious to me that it's either got to have been covered by someone else already, or it's so wrong that I just haven't seen it yet.

For one thing, extending the format limits your extension to that format, unless you craft it in such a way that makes it compatible with other feed formats.  This is not impossible or even hard in some cases, but it's more of a problem of adoption and buy-in than a technical issue.  [`mod_event`][me] is an RSS 1.0 extension; how many RSS 2.0 or Atom 0.3 feeds have you seen using some adaptation of [`mod_event`][me]?  (Though, to be fair, how many RSS 1.0 feeds have you seen using [`mod_event`][me] in the first place?)

Just what do calendar events have to do with syndication feeds, other than that feeds are a convenient carrier wave?  Why should we try to shoehorn calendar data into the fabric of a feed itself?

All the feed formats I care about can carry (X)HTML content, and these [microformats][mf] are just XHTML content constructed along a certain set of conventions.  So, any feed supporting XHTML content can carry microformat-enriched content--without, necessarily, any feed format alterations, convincing of feed format authors, or buy-in from aggregator developers.  (Of course, you might need those developers to actually *do* something with the microcontent when it arrives, but that's another story.)

Leave the feed to manage the business of facilitating push-via-poll with aggregators and decouple the markup and structure of rich microcontent items from feed formats altogether.

Furthermore, this helps address the question of "[Is a feed the right place for your data?][fd]"  My tentative answer to this is, "No, but it doesn't hurt if it's in there, too."  

Think of the feed as just a mechanism to facilitate content delivery--and not as the embodiment of the content itself.  Mind you, [feed entries do make nice representations of content][au], covering many common attributes.  But, keep feeds themselves constructed in terms of metadata about content.  Although items of content might also be carried in full in feed entries, the "*real*" content should exist somewhere else as well.

Things like [`mod_event`][me] should be used to provide *hints* to aggregators whose authors, for instance, might not care to bundle in and maintain a full-blown [microformat][mf] parser.  

Think of a MySQL table:  You can define columns in a table, and then you can define zero or more indexes on those columns.  The data's still there if you don't define any indexes, and queries are still possible--it's just that queries are more laborious.  And, your indexes don't need to be matched up one-to-one with your columns--they can be concatenations of columns, or just about whatever else you want.  

Consider [`mod_event`][me] like an index for aggregators on [hCalendar][hc] content--[hCalendar][hc] defines the columns, [`mod_event`][me] facilitates better routing/filtering.  Although getting buy-in from feed format authors and feed aggregator developers helps get indexes created, you don't necessarily need that to get the content into the feed in the first place.

Okay... I think all that made sense.  I had to get that spewed out of my head before I lost it.  :)

[au]: http://www.decafbad.com/blog/2004/05/17/use_atom_for_a_universal_blog_transfer_protocol
[hc]: http://developers.technorati.com/wiki/hCalendar
[fd]: http://bitsko.slc.ut.us/blog/feed-data.html
[me]: http://web.resource.org/rss/1.0/modules/event/
[rvw]: http://www.pmbrowser.info/wiki.pl?RVW
[mf]: http://developers.technorati.com/wiki/MicroFormats
