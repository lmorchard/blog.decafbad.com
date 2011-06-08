--- 
wordpress_id: 663
layout: post
title: Building a proper shared syndication feed foundation
wordpress_slug: building-a-proper-shared-syndication-feed-foundation
wordpress_date: "2005-06-28T23:21:42-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=663
---
While I'm thinking on the subject of common syndication feed frameworks, it occurred to me that it might be instructive to jot down some thoughts on one of the concerns at the root of my ideas for FeedReactor:  Shared feed fetching, caching, and storage.

I wanted to build something that would intelligently handle all [the issues][h1] [of HTTP][h2] and [feed][s1] [polling][s2] [schedules][s3], across all my apps, all in one spot--once and for all.  Maybe it wouldn't have quite that guarantee of finality, but I'd *hope* to never directly perform an HTTP GET for a feed from one of my apps ever again.

[h1]: http://fishbowl.pastiche.org/2002/10/21/http_conditional_get_for_rss_hackers
[h2]: http://diveintomark.org/tests/client/http/
[s1]: http://www.decafbad.com/blog/2003/09/25/dynamic_feed_scan_times
[s2]: http://www.decafbad.com/blog/2003/09/29/dynamic_polling_freq_too
[s3]: http://www.decafbad.com/blog/2003/11/26/polling_and_urgency

Toward that end, one of my primary requirements is this:  Once I've acquired feed data, I need to store it in some form usable by my other programs and by some method as agnostic as possible toward the actual contents of the feed.  I want to preserve potential extension data, without needing prior knowledge of what that might be.  Extensions are one area where the fun stuff with syndication feeds will be taking off, and I've wanted a foundation to support that.

So, in my tinkering, I've explored four main variations of storing feed data:

1. Fine-grained relational DB tables
2. Triples in an RDF store
3. XML database storage
4. Coarse-grained persistence

### Feeds in relational DB tables

Mapping feed data to relational database tables seems to be the most common approach I've seen in use by aggregators.  Another similar approach involves maintaining a persistent object model.  [Syndication.framework][synd], [NetNewsWire][nnw], [Straw][straw], and [Feed on Feeds][fof] all do something like this, more or less--and I'm sure many others do, as well.   

[synd]: http://www.decafbad.com/blog/2005/06/28/safarirssdb
[fof]: http://feedonfeeds.com/
[nnw]: http://inessential.com/?comments=1&postid=2993
[straw]: http://www.nongnu.org/straw/

The idea is that the raw feed XML comes in, gets parsed, and then methodically dissected to populate columns in a table or properties of an object.  Since the table schema or class definition is planned out ahead of time, only feed data which conforms to this model gets preserved.

Occasionally, an effort is made to "expose all possible data", [ala the Universal Feed Parser][ufp].  But, this is really only practical if your objects are particularly dynamic--and even then [you'll run into issues][nxm], depending on just what shows up in a given feed.  But, if you don't really care much about anything all that exotic in feeds beyond title / link / description, this approach might work out just fine.

[ufp]: http://www.feedparser.org/docs/namespace-handling.html
[nxm]: http://bitsko.slc.ut.us/blog/rdf-longhorn.html

### Feeds as RDF triples

But if you do care about extension data, and if you're going to go through all that trouble of dissecting a feed, you might as well have a sufficiently granular and flexible repository to dump it.  So, how about an RDF triple store?  The underlying model behind RDF can capture anything you can throw at it from syndication feed structures.  In fact, RSS 1.0 and all of its extension modules *are* serialized RDF data.

Here, though, the issue isn't so much a matter of signal loss because pieces don't fit the model.  Instead, the issue is more akin to an impedance mismatch:  

Do you try to transliterate pieces of RSS 2.0 and Atom 0.x feeds into RSS 1.0 parts?  Or do you [recast a feed format like Atom as an RDF vocabulary][atomowl]?  Then, what do you do about all the mostly similar yet slightly different feed bits floating around as triples (i.e. RSS 1.0 vs Atom OWL)?  And, don't even get me started on all the annoyances involved in dismembering and reassembling arrangements of triples--although that's more a function of a particular RDF toolkit.

[atomowl]: http://semtext.org/atom/

### Feeds in an XML database

Admittedly, I haven't done as much as I'd like with feeds in an XML database--such as [Berkeley DB XML][dbxml].  In part, that's been because the various packages have either just been too frustratingly dog-slow or nigh-impossible to get built and running on my OS X development machine.  

[dbxml]: http://www.sleepycat.com/products/xml.shtml

One of the main benefits to this approach--on paper, anyway--is that the feed data stays intact in in the original format as XML.  It doesn't get dismembered, recast, rearranged, or exposed to much of anything that would put any exotic cargo it carries at risk.

But, I think I've got more playing to do with this option.  Although the opportunity to play much more with XSLT, XPath, and XQuery are attractive to me--this seems like potential overkill.  And, whereas the previous two approaches can accommodate a little [liberal parsing][liberal], this approach requires valid feeds.  So, here I'll need to pull in some repair kit tools to normalize and tidy any broken / soupy feeds.  Or, if I'm feeling particularly annoyed, I can just [ignore Postel's Law][plaw] and [pound my fist on the spec][xspec].

[plaw]: http://diveintomark.org/archives/2004/01/08/postels-law
[xspec]: http://www.w3.org/TR/REC-xml#dt-wfc
[liberal]: http://www.xml.com/pub/a/2003/01/22/dive-into-xml.html

### Feeds in coarse-grained persistence

The notion which brought me to this final approach toward storing feed data  goes something like [what this guy wrote][dbmiss]:

> The biggest design mistake of dbXML was making it an XML database. The problem with XML databases is that they store XML, and the problems with XML are too numerous to go into here. Let's just say that processing XML in a native fashion in the database engine itself is a fool's errand, and leads to far too many potential external dependency problems to be worthwhile. If you're doing anything but the simplest of stripped down document storage, It's a much wiser approach to simply store the XML text in a BLOB, delegating the work of schema checking and external entity processing to a higher layer of your system. Otherwise, you can bet your ass that at some point in the feature, when you can least afford for it to happen, something is going to break.

So, in FeedReactor, [that's pretty much what I did][frmodel].  I took Atom feeds and chopped them up into coarse feed and entry chunks, squirreled them away as blobs in a database table, along with a few select columns extracted from the XML data and indexed for easier future retrieval.  

Other than digging for the feed start/end tags and element start/end tags, as well as using a few XPaths to extract those indexed columns, the feed store didn't do anything else other than stow away the XML source.  I left any further handling of the feed data up to XSL and REST API client apps.  

Of course, FeedReactor has been sleeping for quite awhile now, so this is more an idea and an intention than a successfully demonstrated approach.  But, I was eating this dogfood as my main aggregator for the better part of a year, so I think it still has potential.

[frmodel]: http://www.decafbad.com/kwiki/index.cgi?FeedReactorDataModel
[dbmiss]: http://www.tbradford.org/2005/06/advanced-revelation.html

### So, what now?

I'm not sure what quite to do with feeds in a shared way, now and for the future.  Sticking things in a relational database is pretty quick, but very lossy.  Using RDF seems very flexible, but often not too quick or all that friendly.  Calling in an XML database seems like a "good" idea, but my spider sense is tingling.  And finally, chopping feeds up into coarse, vaguely indexed chunks seems less lossy, but not all that elegant.

All in all, maybe it's just enough to download and cache the raw feeds.

I'll post this now, but I'm still thinking about all of this...
