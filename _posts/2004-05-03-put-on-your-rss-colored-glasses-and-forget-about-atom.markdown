--- 
wordpress_id: 519
layout: post
title: Put on your RSS-colored glasses and forget about Atom
excerpt: Well, it did seem quiet, but it's comforting in an odd way that RSS Wars are still raging as I wander back into the blogosphere.  I suggest that all that Atom haters out there put on some RSS-colored glasses and forget there ever was an Atom.  XSLT and URL-as-command-line to the rescue!
date: "2004-05-03T06:39:05-04:00"
wordpress_slug: put-on-your-rss-colored-glasses-and-forget-about-atom
wordpress_url: http://www.decafbad.com/blog/?p=519
---
<blockquote cite="http://grumet.net/weblog/archives/2004/04/28/syndication_and_competing_formats.html"> I know, we've heard a lot about this, and it might seem draining and pointless.</blockquote>
<div class="credit" align="right"><small>Source:<cite><a href="http://grumet.net/weblog/archives/2004/04/28/syndication_and_competing_formats.html">Syndication and competing formats</a></cite></small></div>

Well, it *did* [seem quiet][quiet], but it's comforting in an odd way that RSS Wars are still raging as I wander back into the blogosphere.

And, while [my last post][lastpost] might be seen as a new rock thrown from my direction, it really wasn't meant as such.  I was happy to see [a response from Andrew][response] and a fix.  Oh, and as a bonus, [a fix for my blog][blogfix], to boot!  Now, *that's* the sort of thing I came back for.

Now - as for this renewed RSS vs Atom war.  I've got a pair of RSS-colored glasses for all the Atom haters out there.  Actually, they're not my glasses, but this one guy's [offering a service][service] and this other guy's [offering some XSLT][stylesheets] -- both or either of these can help make all that annoying Atom gibberish look just like RSS to you and your favorite aggregator.  Hooray for the [URL-as-command-line][urlcli]!

For instance, if you hate that [Mark Pilgrim's feed][diveatom] is only available in Atom flavor now, screw him and get it [RSS flavored][diverss] anyway!  The feed even [validates as RSS][diverssvalid].  (Though, if you're in the RSS-loving camp, I'm not sure why you'd want to hear from the likes of *him* anyway.)

You know what this means?  It means you can forget about Atom.  Whenever you see an Atom feed, just put on your RSS-colored glasses.  Hell, if you're an aggregator developer, make the RSS-colored glasses built-in.  You don't even have to embed an XSLT processor in your application: just offer the service from your own web servers and substitute the filter URL automatically when one of your users tries to subscribe to an Atom feed.  

(Though, you know, it would be awfully nice of you to throw in an XSLT processor.  At least one aggregator author thinks it's [a good idea][goodidea].  So does [this user / customer][goodidea2].  But, it's admittedly an idea bordering on NeatLikeDigitalWatches.)

Or, get this: borrow a service or a stylesheet hosted by an Atom sympathizer.  If there's demand and I feel like taking some abuse, I'll host such a service right here.  (Though I'd likely live to regret doing *that*!)  In fact, using a set of RSS-colored glasses maintained by an Atom sympathizer is the best thing.  Let that poor altruistic sucker keep up with the rapid pace of change in the Atom world, updating XSLT, while you just happily go on seeing the world in RSS.

There.  Problem solved.  Let's move onto more exciting projects.  

(He writes, knowing that it's never that simple.  And that he's likely to get bludgeoned for this.  And that he talks about himself in the third person far too often and makes too many parenthetical digressions.)

But, I digress...

[goodidea2]: http://weblogs.cs.cornell.edu/AllThingsDistributed/archives/000454.html
[goodidea]: http://nick.typepad.com/blog/2004/04/new_gray_boxes_.html
[urlcli]: http://udell.roninhouse.com/bytecols/2001-08-15.html
[diveatom]: http://diveintomark.org/xml/atom.xml
[diverss]: http://cavedoni.com/2004/02/rss1?uri=http://diveintomark.org/xml/atom.xml
[diverssvalid]: http://rss.scripting.com/?url=http%3A%2F%2Fcavedoni.com%2F2004%2F02%2Frss1%3Furi%3Dhttp%3A%2F%2Fdiveintomark.org%2Fxml%2Fatom.xml
[stylesheets]: http://www.aaronland.info/xsl/atom/0.3/
[service]: http://cavedoni.com/2004/02/rss1
[blogfix]: http://www.decafbad.com/blog/2004/05/02/feed_validation_confusion#comment-1114
[response]: http://www.decafbad.com/blog/2004/05/02/feed_validation_confusion#comment-1113
[lastpost]: http://www.decafbad.com/blog/2004/05/02/feed_validation_confusion
[quiet]: http://www.decafbad.com/blog/2004/04/29/has_it_been_quiet
