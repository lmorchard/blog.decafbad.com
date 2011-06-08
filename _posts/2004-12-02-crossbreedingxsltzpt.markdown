--- 
wordpress_id: 570
layout: post
title: Cross-breeding XSLT and ZPT
excerpt: Both ZPT and XSLT very different technologies, but they are often used in similar contexts.  More than once, I've wished that XSLT was as simple as ZPT (i.e. less verbose and intrusive, more document centered), and I've wished that ZPT had some of the features of XSLT (i.e. ability to be used as a transforming filter).
tags: 
- xml
- python
wordpress_slug: crossbreedingxsltzpt
wordpress_date: "2004-12-02T20:15:52-05:00"
wordpress_url: http://www.decafbad.com/blog/?p=570
---
I've recently been doing some side work involving Zope and, along with the rest of the suite of technologies it offers, I've been happy to be working with [Zope Page Templates](http://dev.zope.org/Wikis/DevSite/Projects/ZPT/FrontPage) again.  I dabbled with them a bit when they first came out, and a Zope-free implementation named [SimpleTAL](http://www.owlfish.com/software/simpleTAL/) was one of the core components of the iteration of my news aggregator which came before FeedReactor.

Out of all the templating and content generation approaches I've used, Zope Page Templates are my favorite yet.  Pretty expressive, yet unobtrusive; nicely powerful, yet not quite something with which you'd want to write an entire application ([and that's a feature, not a bug](http://naeblis.cx/rtomayko/2004/12/02/a-note-on-template-design)).  
  
I've yet to be in a work-a-day team that uses ZPT-- but I can see where a lot of production, delegation, and integration issues would have gone much smoother had I used ZPT instead of [Template Toolkit](http://www.template-toolkit.org/) for the web app framework I created at a previous company.  (Though I do have to say TT2 is *very* nicely done!)  And where I am now, I spend most of my days trying to pummel ASP 3.0 pages into some semblance of logic/presentation separation-- I would certainly dive at the chance to dump VBScript and `<% cruft %>` for a bit of Python and ZPT.  (But, you know, *it's a living*.)
   
A close second favorite is XSLT.  I've really been hot on it lately, having worked it into the core of FeedReactor in place of SimpleTAL.  And in [other](http://www.decafbad.com/blog/2003/09/02/xsl_scraper) [hacks](http://www.decafbad.com/blog/2004/06/16/wishofthemonthclub1), I've really come to appreciate it's role as a filter segment in pipelines between REST web services and [URL-as-command-line](http://udell.roninhouse.com/bytecols/2001-08-15.html) invocations.

Granted, both ZPT and XSLT very different technologies, but they are often used in similar contexts.  More than once, I've wished that XSLT was as simple as ZPT (i.e. less verbose and intrusive, more document centered), and I've wished that ZPT had some of the features of XSLT (i.e. ability to be used as a transforming filter).

Reading [Ryan Tomayko's description of Kid](http://naeblis.cx/rtomayko/2004/11/30/pythonic-xml-based-templating-language) got me thinking, and googling.  One thing I turned up from a mailing list archive asked about an &#8220;[XSL implementation of TAL?](http://mail.zope.org/pipermail/zpt/2002-January/002651.html)&#8221;  It struck me as a tad nutty at first, but then I started having inklings that just maybe it could be done.  (Whether it *should* be done, well...)  But the kernel of the idea grabbed me: Instead of using [TALES path expressions](http://zope.org/Wikis/DevSite/Projects/ZPT/TALES%20Specification%201.3) to look up values in Pythonic space, why not use XPath expressions to look up values from a supplied XML document?

This strikes me as such an obvious idea that someone has to already have done it and possibly rejected it for good reason.  On the other hand, maybe this is the sort of thing Ryan's thinking about-- I wonder how hard it would be to hack this into Kid?  It would give only a subset of XSLT's capabilities in trade for simplicity, and would only offer the &#8220;[pull](http://www.dpawson.co.uk/xsl/sect2/pushpull.html)&#8221; approach, but it would give XML-pipelining to a ZPT-ish technology.

I think this is something I want to look into a bit further at some point.
<!--more-->
shortname=crossbreedingxsltzpt
