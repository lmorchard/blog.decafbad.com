--- 
wordpress_id: 1048
layout: post
title: Say hello to FeedMagick2
tags: 
- webdev
- rss
- php
- atom
- xml
- feedmagick
- feedmagick2
- feeds
wordpress_slug: say-hello-to-feedmagick2
wordpress_date: "2007-04-29T23:06:32-04:00"
wordpress_url: http://decafbad.com/blog/2007/04/29/say-hello-to-feedmagick2
---
Yeah, things have been basically silent around here thanks to post-work brain fryage and a general lack of things to say.  Really, everyone else around the blogosphere seems to be covering things satisfactorily.  However, I have been idly working on a new project over the past few weeks, namely a total rewrite and redesign of [my format-ignorant feed filtering and munging kit dubbed FeedMagick](http://decafbad.com/blog/?s=feedmagick).

You can find [a demo installation of FeedMagick2 here](http://decafbad.com/2007/04/FeedMagick2/) and find it [ready for checkout from SVN over here](http://decafbad.com/svn/trunk/FeedMagick2/).  It's basically just a step away from being a proof of concept, but I'm hoping to get around to fleshing out docs and battening down the hatches with tests.  In any case, if my serial enthusiasm holds out, this thing could eventually subsume everything else I've done with feeds.

For now, peek at some of these highlights:

   * [Master Personal Feed](http://decafbad.com/2007/04/FeedMagick2/inspect/masterfeed) - One big feed blended from 10 other personal metadata feeds pulled from various Web-2.0-ish sites.
   * [Feed to JSON via Magpie](http://decafbad.com/2007/04/FeedMagick2/inspect/magpiejson) - Get feed data parsed by way of [Magpie](http://magpierss.sourceforge.net/) into JSON data structures
   * [Flickr Favorites Feed](http://decafbad.com/2007/04/FeedMagick2/inspect/flickrfavorites) - Feed of photos marked as favorites by a Flickr user, pulled via the API
   * [jbox.com scraper](http://decafbad.com/2007/04/FeedMagick2/inspect/jbox) - Pipeline composed of [HTML Tidy](http://tidy.sourceforge.net/) and XSL to scrape [jbox.com](http://jbox.com/) to build an RSS feed of new items for sale.

Beyond practical examples, there are some things under the hood that seem keen to me.  Apropos of my [pipes-via-web ramblings](http://decafbad.com/blog/2007/02/15/thoughts-on-pipes-on-the-web-part-ii) back in February, I'm trying out a few different approaches to pipelining feed content through processor modules.  My original FeedMagick relied on feeding URLs to URLs as parameters.  That, unfortunately, can be mighty cumbersome and inefficient.  So, FeedMagick2 explores a few more approaches:

   * The first and obvious approach is to chain them together in a single script.  So, I've got objects instances that pass content from one to the next.  The thing is, the pipe works in reverse:  The driver script asks the last module in the pipe for content, which then asks the one before it for content, and so on.  At any point along the way, modules can cache the output of previous modules, and refrain from calling up the chain.

   * The second way to chain pipelines together is just like the first FeedMagick:  Some pipelines start with fetching a URL.  That can be an original feed, or a URL leading to the output of an antecedent pipeline.  And, oh yeah, most pipelines are run via parameterized URLs, so there's that bit of handy recursion.

   * The third way to chain pipelines together is with HTTP POST:  A pipeline can accept feed data via the request body of an HTTP POST, thus allowing antecedent pipelines (or even cURL scripts) to *push* data into the pipeline rather than getting *pulled* via URL.  This is kind of like my [years-old jiggery pokery](http://decafbad.com/blog/?s=xmlrpc+pipe) with [pipelines via XML-RPC](http://www.decafbad.com/twiki/bin/view/Main/XmlRpcFilteringPipe), only much *much* simpler.

I'm also poking around at making all of the above available at the command line via PHP-CLI, and I'm having gratuitous fun exploring PEAR to roll my own stripped-down web framework.  I still hate PHP, but I'm at least finding ways to entertain myself while I'm holding my nose.  Of course, I find weird things entertaining.

And, as a side note, the only reason I'm using PHP is because I'd like to play around with the idea of the de facto WordPress installation requirements standard.  That is:  If you can run WordPress, you can run this.  In reality, I don't think I'm there, but I'm hoping to get close.  For one, I'm refusing to play with anything older than PHP 5.

Anyway, play with it, tell me what you think and give me a reason to keep hacking at it.  :)
