--- 
wordpress_id: 546
layout: post
title: Early dbagg3 demo is alive and kicking
excerpt: So at this point, it's all URLs and barely working HTML, but it's exciting to me at least.  And it's dogfood for me, since I'm using this crud to get my daily (hourly?) fix.  Pretty soon, I'll be diving into wrapping more of a proper usable web app around this, with user management and stuff that works in MSIE.  Until then, maybe someone else will see this and catch a buzz from it.
wordpress_url: http://www.decafbad.com/blog/?p=546
---
Got some very good work in this weekend on switching servers and getting [`dbagg3`][dbagg3] in some semblance of working order somewhere other than on my overworked and decidedly non-publicly-demonstrable laptop.

This stuff is so this side of premature, that I'm probably about to cause [JohnCompanies][johncompanies] to send hit-men out to cancel **me**, along with my hosting account (have I said that I *really* appreciate the help so far?).  But I just have to get this out: I'm easily excited by shiny code and gadgets, but it's so much easier to get excited when I can see something in working condition before taking a screwdriver to it.  So... remember [when I mentioned all those URLs][dbagg3urls]?  They're working out nicely.

First, check out a simple two-pane view of news items, ala [Bloglines][bloglines]:

* <a href="http://feeds.decafbad.com/api/users/demo.xml?xsl=xsl/two-pane/index.xsl&#38;content-type=text/html" target="new">http://feeds.decafbad.com/api/users/demo.xml?xsl=xsl/two-pane/index.xsl&#38;content-type=text/html</a>

Taking this apart, you can see:

* A user account: <http://feeds.decafbad.com/api/users/demo.xml>
* Some XSL: <http://feeds.decafbad.com/xsl/two-pane/index.xsl>
* ... and a specified content type (text/html)

If your curiosity is piqued by this, view source and pay attention to link URLs.  It's more of the same:  XML produced by a REST API, passed through XSL, delivered as HTML.

Here, take a look at another view on this demo user's aggregated items:

* <a href="http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/outliner/index.xsl&#38;content-type=text/html" target="new">http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/outliner/index.xsl&#38;content-type=text/html</a>

Unfortunately, this only seems to be working decently with Firefox and Safari.  MSIE seems to be balking at the dynamic stuff, though I've had it working there in a previous incarnation of this code.  So hopefully this will be fixed soon.

At any rate, what you should see is a single-pane outliner-style display of feed entries.  This is the style of aggregator UI I've been using for almost 3 years now.  Disclosure triangles open entries up to show summaries and further content.  &#8220;[seen]&#8221; links hide the entries, while &#8220;[queue]&#8221; hides an entry while tossing it into a queue for viewing later.

Speaking of that, you can see what's in the queue right now:

* <a href="http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/full.xsl&#38;content-type=text/html&#38;show_queued=1" target="new">http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/full.xsl&#38;content-type=text/html&#38;show_queued=1</a>

Here is a display of queued entries, with another stylesheet applied that shows everything in a flat and open blog-like template.  It's not reverse-chronological, but that's not hard to accomplish with a flag or a tweak to an &lt;xsl:sort&gt; tag.  

So that's just the start of things.  Remember [when I was rambling on about XML storage and query][dbagg3storage]?  A URL like this is one product of that:

* <a href="http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/full.xsl&#38;content-type=text/html&#38;entry_xpath=//entry/title[contains(text(),'OS%20X')]" target="new">http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/full.xsl&#38;content-type=text/html&#38;entry_xpath=//entry/title[contains(text(),'OS%20X')]</a>

This should show you a flat listing of all entries whose titles contain &#8220;OS X&#8221;.  This is far from perfect, but it's very exciting to me-- it's got a lot of promise, stuff that first caught my eye when I saw [Jon Udell playing][xpathquery] [awhile back][xpathquery2].

Now, something that you might not notice until doing a bit more digging, is that all these attributes like &#8220;seen&#8221; and &#8220;query&#8221; are annotations made by the user on entries.  If you take a peek at [some of the Javascript][js] under the hood, you might notice some XmlHTTPRequest code going on.  To mark something as &#8220;seen&#8221; or &#8220;queued&#8221;, I POST XML to a URL like this:

* http://feeds.decafbad.com/api/users/demo/subscriptions/638/entries/60567/notes/

The upshot of this is that these attributes are not limited to &#8220;seen&#8221; or &#8220;queued&#8221; flags-- in fact, these annotations can (well, in theory) be any pairing of arbitrary XML and a name.  This annotation then gets injected into the entry, when viewed by the user who owns the annotation, like so:

* http://feeds.decafbad.com/api/users/demo/subscriptions/638/entries/60567.xml

In fact, you could invent a new annotation called 'tags' and filter for entries with this annotation with a URL like this:

* http://feeds.decafbad.com/api/users/demo/subscriptions/now-12.xml?xsl=xsl/full.xsl&#38;content-type=text/html&#38;entry\_notes\_xpath=//dbagg3:note[@name='tags' and contains(text(),'#food#') and contains(text(),'#odd#')]

Eventually, what I'd *really* like to see this start doing is something akin to del.icio.us-style tagging while you're reading.  Then, you can have public queries that pull feeds based on your (and others') tags and spit things back out as feeds again with the proper XSL stylings.

So at this point, it's all URLs and barely working HTML, but it's exciting to me at least.  And it's dogfood for me, since I'm using this crud to get my daily (hourly?) fix.  Pretty soon, I'll be diving into wrapping more of a proper usable web app around this, with user management and stuff that works in MSIE.  Until then, maybe someone else will see this and catch a buzz from it.

Stay tuned.

[js]: http://feeds.decafbad.com/js/agg.js
[xpathquery2]: http://webservices.xml.com/pub/a/ws/2003/06/10/xpathsearch.html?page=1
[xpathquery]: http://webservices.xml.com/pub/a/ws/2003/04/15/semanticblog.html
[johncompanies]: http://www.johncompanies.com
[dbagg3storage]: http://www.decafbad.com/blog/2004/08/23/slicing_and_dicing_to_make_atom_soup_in_dbagg3
[dbagg3urls]: http://www.decafbad.com/blog/2004/08/30/dbagg3_makingprogress
[dbagg3]: http://www.decafbad.com/cvs/dbagg3/
[bloglines]: http://www.bloglines.com/
<!--more-->
shortname=dbagg3alive
