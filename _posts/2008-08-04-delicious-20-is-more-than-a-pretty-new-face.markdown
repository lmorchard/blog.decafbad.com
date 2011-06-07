--- 
wordpress_id: 1239
layout: post
title: Delicious 2.0 is more than a pretty new face
wordpress_url: http://decafbad.com/blog/?p=1239
---
I'm no longer at Yahoo! and I no longer work on [Delicious](http://delicious.com), but I'm still a huge supporter.  And, since I'm pretty sure everyone over there is either burnt out or still insanely busy at the moment, it might be awhile before anyone tells the full story of what this relaunch offers.  As it is, even I only know a bit of what all went into this effort.

So, off the top of my head, I thought I might point out **just a few** of the easily-missed improvements the new site offers beyond the great new love-it-or-hate-it visual redesign that seems to have occupied most of the discussion I've seen so far:

**Search works and is incredibly fast.**  In fact, search may really be the real star of the redesign show here—especially since del.icio.us often took 30 seconds or more for a simple search, rendering it all but useless.  Today, though, it's at ludicrous speed in comparison—and so finally, the real power of search applied to social bookmarking might start to shine with the critical mass of content found by real people using Delicious.

To scratch my own itch, I've created [an unofficial OpenSearch search engine plugin for Delicious](http://mycroft.mozdev.org/developer/devlist.html?email=l.m.orchard%40pobox.com) on Mycroft.  Though I think it comes along with [the browser extensions](http://delicious.com/help/tools), I've yet to find this for [autodiscovery](http://mycroft.mozdev.org/developer/hosting.html) from the site itself.

**The notes field in bookmarks has been expanded from 255 to 1000 characters.**  Yes, this means that you can now include long running quotes from pages, or complete paragraphs of rambling discourse. 

**[The feeds have all been overhauled and reorganized](http://delicious.com/help/feeds).**  An attempt at backward compatibility was made, but the old feed URLs are all deprecated.  Replacing these, there's now [a common and consistent URL namespace for feeds across formats](http://delicious.com/help/feeds).  

Almost all RSS feeds have [JSONP](http://bob.pythonmac.org/archives/2005/12/05/remote-json-jsonp/) counterparts, and further feed formats could be considered.  Additionally, the old mix of RSS 1.0 and 2.0 has been dropped in favor of RSS 2.0 format across the board to support podcast and media enclosure elements consistently.  The [linkrolls, tagrolls, network badges, and tagometers](http://delicious.com/help/tools) now all use the new JSONP feeds—and the widgets can be examined as example code in using the feeds.

**Tag bundles can now be viewed as combined bookmark views, complete with feeds.**  This augments bundles from a simple visual organization tool to a more powerful content aggregation function.  Personally, I never had much use for tag bundles until now, but since they can actually be used to partition tags and bookmarks I might actually take the time to use them.  Check out these example URLs:

* [http://delicious.com/britta/bundle:art%2Fdesign](http://delicious.com/britta/bundle:art%2Fdesign)
* [http://feeds.delicious.com/v2/rss/britta/bundle:art%2Fdesign](http://feeds.delicious.com/v2/rss/britta/bundle:art%2Fdesign)

**Bundles now work for tags, network contacts, and subscriptions.**  This means, for example, that you can partition your network contacts into topical groups.  From there, you can subscribe to those partitioned bookmarks in different folders in readers, or use the bundled bookmark views in mashups through JSON feeds.  Check out these example URLs:

* [http://delicious.com/network/bkerr/bundle:Brickyard](http://delicious.com/network/bkerr/bundle:Brickyard)
* [http://feeds.delicious.com/v2/rss/network/bkerr/bundle:Brickyard](http://feeds.delicious.com/v2/rss/network/bkerr/bundle:Brickyard)

**Network member and fan feeds now include the date when the contact was added.**  Pro tip: Subscribe to fan feeds to see when new people have started following your bookmarks.

**[Several previously undocumented parts of the V1 API have now been documented](http://delicious.com/help/api).**  In particular, the following new parameter combinations have been used with the browser extensions for primitive bookmark sync:

* https://api.del.icio.us/v1/posts/all?hashes
* https://api.del.icio.us/v1/posts/all?meta=yes
* https://api.del.icio.us/v1/posts/all?fromdt={DT}&todt={DT}
* https://api.del.icio.us/v1/posts/all?start={##}&results={##}

**The posts/all API URL works again for users with large collections.**  With my 11k+ bookmarks, del.icio.us was keeling over with the attempt to assemble and deliver my entire collection with a posts/all call.  Now, however, Delicious 2.0 appears able to handle this call for my account.

**Easter eggs have been rotated and recalibrated.** No, I'm not going to tell you what or where or how many they are.
