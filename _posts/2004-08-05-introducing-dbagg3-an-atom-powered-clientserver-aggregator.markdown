--- 
wordpress_id: 536
layout: post
title: Introducing dbagg3, an Atom-powered client/server aggregator
excerpt: |-
  It's a new feed aggregator, my third attempt at such.  Everything is clunky and command-line driven at present--but I've got further plans, like a REST API for feed queries and manipulation of various things such as feed subscriptions and the read/unread state of items.  Pair this with an XSLT-driven browser UI, and the possibility of other clients (not the least of include other Atom-consuming aggregators).
  
  The goal is to make a Client/Server Aggregator.
tags: 
- syndication
- python
wordpress_slug: introducing-dbagg3-an-atom-powered-clientserver-aggregator
wordpress_date: "2004-08-05T09:04:56-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=536
---
**Update**: I've just dumped what code I have into my CVS repository.  So, go ahead and poke fun at it:

   * <http://www.decafbad.com/cvs/dbagg3/>

Or, fetch it from CVS:

    $ cvs -d:pserver:anoncvs@www.decafbad.com:/cvsroot login
    (Logging in to anoncvs@www.decafbad.com)
    CVS password: anoncvs
    $ cvs -d:pserver:anoncvs@www.decafbad.com:/cvsroot co dbagg3

* * *

So, besides the funk, there's a little project in which I've gotten immersed.  Here's a teaser diagram:

<img src="http://www.decafbad.com/2004/08/dbagg3-demo/dbagg3-phase1.jpg" />

It's a feed aggregator, my third attempt at such.  At present, things are roughly close to the diagram above.  Everything is clunky and command-line driven at present--but I've got further plans, like a REST API for feed queries and manipulation of various things such as feed subscriptions and the read/unread state of items.  Pair this with an XSLT-driven browser UI, and the possibility of other clients (not the least of include other Atom-consuming aggregators).

The goal is to make a [Client/Server Aggregator][clientserveragg].  Somewhat serendipitously, I just caught Bob DuCharme's xml.com [article on Amazon.com's web services][amazonrest], which [I really like][wishes] and have drawn inspiration from in thinking about this new aggregator.  Eventually, I want to offer the same sort of XML+XSL style of service that they've put together, along with some futher inspiration from the [Atom API][atomapi].  

Anyway, as another teaser, check out this early demo involving the XML this thing has been producing, coupled with some experimental XSL:

* [dbagg3 demo page][dbagg3demo]

You'll notice that there are three URLs involved here:

* [An XSLT processor service][dbagg3xsltproc]
* [An XSLT stylesheet][dbagg3xsl]
* [Some aggregated Atom feeds][dbagg3xml]

The XSLT expects Atom (plus a few extensions of my own), so you can also do things like this:

* [Dive Into Mark][mark]
* [Intertwingly][sam]
* [0xDECAFBAD][me]

These are the sorts of tricks I was looking forward to when I started thinking about things like a [universal blog transfer format][blogxfer] and [rose-colored glasses][roseglasses].  XSLT used like this could just as easily produce a blog or RSS 2.0 content.

Anyway, hoping to get some code into CVS by this weekend that's not entirely embarassing.  So if you're interested in this stuff, stay tuned.  I'm hoping that this thing can provide a base for others interested in feed aggregation--if you just want to play with UI, use the scanning and storage as-is and tinker with XSLT; if you want to play with storage and query, leave the scanning and UI alone; if you want to tinker with parsing... er, [talk to Mark Pilgrim][ufp].

More soon!  

(Oh yeah, and I *will* be working on coming up with a better name than `dbagg3`.  Unfortunately, I probably won't be coming up with a more visually appealing design for the UI, since what you see is the best I can do.  Heh, heh.  Don't let your programmers do visual design...)

[atomapi]: http://www.atomenabled.org/developers/api/atom-api-spec.php
[urchin]: http://urchin.sourceforge.net/
[ufp]: http://www.feedparser.org/
[roseglasses]: http://www.decafbad.com/blog/2004/05/03/put_on_your_rsscolored_glasses_and_forget_about_atom
[blogxfer]: http://www.decafbad.com/blog/2004/05/17/use_atom_for_a_universal_blog_transfer_protocol
[me]: http://www.decafbad.com/2004/08/dbagg3-demo/xsltproc.cgi?xsl=http://www.decafbad.com/2004/08/dbagg3-demo/new.xsl&#38;xml=http://www.decafbad.com/blog/atom.xml
[sam]: http://www.decafbad.com/2004/08/dbagg3-demo/xsltproc.cgi?xsl=http://www.decafbad.com/2004/08/dbagg3-demo/new.xsl&#38;xml=http://www.intertwingly.net/blog/index.atom
[mark]: http://www.decafbad.com/2004/08/dbagg3-demo/xsltproc.cgi?xsl=http://www.decafbad.com/2004/08/dbagg3-demo/new.xsl&#38;xml=http://www.diveintomark.org/xml/atom.xml
[dbagg3xsltproc]: http://www.decafbad.com/2004/08/dbagg3-demo/xsltproc.cgi
[dbagg3xsl]: http://www.decafbad.com/2004/08/dbagg3-demo/new.xsl
[dbagg3xml]: http://www.decafbad.com/2004/08/dbagg3-demo/demo.xml
[awsrss]: http://www.decafbad.com/2004/03/xml-rss091.xsl
[dbagg3demo]: http://www.decafbad.com/2004/08/dbagg3-demo/xsltproc.cgi?xsl=http://www.decafbad.com/2004/08/dbagg3-demo/new.xsl&#38;xml=http://www.decafbad.com/2004/08/dbagg3-demo/demo.xml
[clientserveragg]: http://www.intertwingly.net/wiki/pie/ClientServerAggregator
[amazonrest]: http://www.xml.com/pub/a/2004/08/04/tr-xml.html
[wishes]: http://www.decafbad.com/blog/2004/06/16/wishofthemonthclub1
