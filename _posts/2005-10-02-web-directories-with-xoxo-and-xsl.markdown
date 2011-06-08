--- 
wordpress_id: 712
layout: post
title: Web directories with XOXO and XSL
tags: 
- xoxo
- microformats
- opml
- gopher
wordpress_slug: web-directories-with-xoxo-and-xsl
wordpress_date: "2005-10-02T23:50:17-04:00"
wordpress_url: http://decafbad.com/blog/?p=712
---
Now, in my [previous post][prev], I'd mentioned that I might have some ideas to "put up" in response to this recent OPML and web directories kerfluffle.  Here's my general idea:

How about trying [XOXO][], [the `rel` attribute on HTML links][rel], and [the `subsection` link type][subsection]—all with a bit of XSL to make it work?

Here's some working data and code:

  * [Here's the end result][end], a simple web directory.
  
Here are some clues as to what the above does:

  * This directory started with [this top-level outline][master].  View source on this page, notice the "Syndication Feeds" link with the `rel="subsection"`.
  * Applying [this XSL][xsl] using [this web service][xsltproc] is where the work gets done.  This consists of dereferencing each link with a `rel="subsection"` and transcluding the innards of the page at the end of the URL.
  * Notice that [the URL of "Syndication Feeds"][ex2] comes from a domain other than `decafbad.com`.  If I wanted to, the [third level of transclusion][ex3] could've come from yet another domain, too.
  
I think this solution is better than using OPML for web directories.  Although it could use some refinement—using a bit of `<iframe>` or AJAX magic to include in a page, perhaps—it's not only *already supported* by more applications than OPML, it *also* leverages a lot of prior art and consensus work.  

So, am I wrong here?  If so, please tell me how, where, and why.

[ex3]: http://hackingfeeds.com/2005/10/xoxo-transclude/ex3.html
[ex2]: http://hackingfeeds.com/2005/10/xoxo-transclude/ex2.html
[xsltproc_src]: http://decafbad.com/2005/10/xoxo-transclude/xsltproc.txt
[xsltproc]: http://decafbad.com/2005/10/xoxo-transclude/xsltproc
[xsl]: http://decafbad.com/2005/10/xoxo-transclude/xoxo-transclude.xsl
[master]: http://decafbad.com/2005/10/xoxo-transclude/ex1.html
[end]: http://decafbad.com/2005/10/xoxo-transclude/xsltproc?xslAddr=xoxo-transclude.xsl&amp;docAddr=ex1.html
[subsection]: http://www.w3.org/TR/REC-html40/types.html#type-links
[rel]: http://www.w3.org/TR/REC-html40/struct/links.html#h-12.2
[xoxo]: http://microformats.org/wiki/xoxo
[prev]: http://decafbad.com/blog/2005/10/02/a-kerfluffle-of-opml-and-web-directories
