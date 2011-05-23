--- 
wordpress_id: 797
layout: post
title: More on ignorant feed handling
wordpress_url: http://decafbad.com/blog/?p=797
---
Part of the reason this whole [must ignore][mi] thing with respect to feeds has me [a bit fired up][fir] is because it seems like so few feed processing tools out there embrace this idea.  And because of that, these tools are unfortunately brittle and prone to future shock.

For example, take [`Syndication.framework` on OS X][sx]:  Amongst the monkeys and ninjas and pirates and robots, you've got your standard *title-date-link-description* columns with a few other bits for good measure.  But, where's the data from [iTunes RSS extensions][ir]?  Nowhere, gone, lost.  If it was in the feed when `Syndication.framework` found it, it wasn't understood and so it wasn't retained after the parser finished chewing up and spitting the data into that DB table.

[I've written about shared feed processing foundations before][sf], but I don't think I've totally gotten the idea to gel in my head until now.  Here's the thing:  If you want feed processing tools that are useful for the general case, they have to be tolerant of things not understood.  Rather than intrusively breaking apart and recasting feed data into a predetermined data structure, you've got to remain hands-off as much as possible.

This is what I did in [FeedSpool][fs].  This code can subscribe to feeds, poll feed data periodically, and even work out which items in a feed are newâ€”but it punts on everything else by only caring about where a feed starts and ends, and where its individual entries start and end.  *The rest is left in its original XML form.*  So, if there was data in there for iTunes?  It's still there, because [FeedSpool][fs] didn't know enough to do anything to it.

This is the major difference in feed processing model.  `Syndication.framework` loses information when it encounters things it doesn't understand.  [FeedSpool][fs] retains the information, because it leaves things alone when it doesn't know any better.

Now, this is not to pick on just `Syndication.framework`.  Despite the general-sounding name,  this framework is pretty much just around to power [Safari RSS][sr] and not [iTunes][itp] or anything else.  And as I said, pretty much every other feed processing framework and tool works in this manner.  Just about everybody uses a destructive process when they parse and marshal feed data into local-idiom structures.  

And this destructive process is fine when all you want to do is satisfy a specific purposeâ€”display a few headlines, for example.  But if you're trying to build general-case feed plumbing, this is unacceptable and untenable.  If most everything in a feed item gets lost as it goes through a pipeline, [we might as well abandon feed extensions entirely in favor of microformats stuffed into the `description` tag][fmf]â€”an idea to which I'm not *entirely* opposed.

On the other hand, consider this:  This past summer, [Microsoft released an architectural overview about an OS-wide RSS framework in the upcoming Vista][ao].  Unfortunately, like many RSS and Vista related things from this past summer, all links have evaporated into a redirect to a single developers portal.  I can't figure out why they didn't just [redirect over to here][he], which took me a search and a few clicks to rediscover.

At any rate, there's one sentence in this overview that gives me hope for RSS as a general service in Windows Vista:  

"*It is also possible to access the item XML for applications that want to perform operations on the XML instead of using the item's properties.*"

So, dig that.  If it works the way I hope it does, RSS in Vista will take care of the subscriptions for you, poll the feed data, grab new stuffâ€”but then it leaves the data intact for you to process whatever new and unanticipated feed payloads that may arrive.

That's how it *should* work.

[fmf]: http://decafbad.com/blog/2005/05/05/the-right-place-for-data-in-your-feed
[itp]: http://www.apple.com/itunes/podcasts/
[fir]: http://decafbad.com/blog/2005/12/13/feedmagick-the-feed-filter-that-doesnt-know-much-about-feeds
[sr]: http://www.apple.com/macosx/features/safari/
[he]: http://msdn.microsoft.com/windowsvista/building/rss/default.aspx?pull=/library/en-us/dnlong/html/rsssupportinlonghorn.asp
[tc]: http://msdn.microsoft.com/windowsvista/integrated/
[ao]: http://decafbad.com/blog/2005/06/28/four-thoughts-on-ms-rss-so-far
[fs]: http://decafbad.com/trac/wiki/FeedSpool
[ir]: http://phobos.apple.com/static/iTunesRSS.html
[sx]: http://decafbad.com/blog/2005/06/28/safarirssdb
[sf]: http://decafbad.com/blog/2005/06/28/building-a-proper-shared-syndication-feed-foundation
[mi]: http://www.xml.com/pub/a/2004/10/27/extend.html
