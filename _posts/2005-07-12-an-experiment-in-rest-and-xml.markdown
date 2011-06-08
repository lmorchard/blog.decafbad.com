--- 
wordpress_id: 668
layout: post
title: An Experiment in REST and XML
wordpress_slug: an-experiment-in-rest-and-xml
wordpress_date: "2005-07-12T23:10:38-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=668
---
Okay, so I finally got the second of today's demos running on the server here.  Take a look at this chunk of a shell transcript:

* [http://www.decafbad.com/2005/07/xmlwiki/doc/log.txt](http://www.decafbad.com/2005/07/xmlwiki/doc/log.txt)

One of the first things this should show is just how great [cURL][curl] can be for testing REST-based web services.  The second thing you should see is the web service I threw together at this URL:

* [http://www.decafbad.com/2005/07/xmlwiki/www/store](http://www.decafbad.com/2005/07/xmlwiki/www/store)

Here's the gist: I'm trying to make something like a cross between an XML database and a wiki, with a REST API.  The URLs in the system give access to the XML documents as resources.  Not only that, you can navigate paths into elements in the XML files themselves.  

These URLs mostly support GET, PUT, and DELETE HTTP methods.  (No POST, yet.)  You can GET documents and elements within documents.  You can PUT documents and replace elements within documents.  You can DELETE documents and elements within documents.

This thing is barely useful in its present state, but I'm hoping to work a little XmlHTTPRequest mojo to join [my outliner][outliner], [some paragraph editing][qmpara] with some [purple number][pn] inspiration, and [maybe][d0] [a few][da] [other][d1] [things][d2] together into something interesting.

But, who knows if I'll ever get the pieces together--or if I've even got my head on straight about how all this will work.  I'm throwing this out there in a very early, probably broken state in the hopes of getting a sanity check or maybe giving someone else some useful code if I wander off and abandon it.

Speaking of the code, look over here in my Subversion repository:

* [http://www.decafbad.com/svn/trunk/xmlwiki/](http://www.decafbad.com/svn/trunk/xmlwiki/)

There's not much there yet, and some of it is half broken stuff I hope to make work with [Berkeley DB XML][dbxml], but there you have it.

[pn]: http://www.eekim.com/software/purple/purple.html
[dbxml]: http://www.sleepycat.com/products/xml.shtml
[da]: http://www.decafbad.com/blog/2004/12/23/abook1
[d0]: http://www.decafbad.com/blog/2004/11/30/nextgenwebapps
[d1]: http://www.decafbad.com/blog/2005/07/02/css_treemaps
[d2]: http://www.decafbad.com/blog/2005/07/02/drag_the_boxes_stretch_the_lines
[qmpara]: http://www.quirksmode.org/dom/cms.html
[outliner]: http://www.decafbad.com/blog/2005/07/12/xoxo_outliner_experiment
[curl]: http://curl.haxx.se
