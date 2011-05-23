--- 
wordpress_id: 643
layout: post
title: What's old (scraping) is new again (microformats)
wordpress_url: http://www.decafbad.com/blog/?p=643
---
You know, I think I fully realized why microformats seem so appealing and familiar to me:

The appealing part stems from that fact that I've been working on building web scrapers for years now, using a slew of languages (Perl, Java, Python, XSL, JavaScript, bash scripts) and approaches (HTML parsing, regexes, XSL, tidy-and-XPath).  Anything to make that easier strikes a nice chord with me.

But, I just remembered that a few summers ago, I wrote a bit for [the O'Reilly book Spidering Hacks][sh] that anticipates the notion of a microformat.  

If you happen to have the book (which I highly recommend), or can read it on [Safari][sa] (which I also highly recommend), take a look at **Hack #96: Making Your Resources Scrapable with Regular Expressions**.

Granted, my proto-solution published there suggested using regexes and consistenly named HTML *id* attributes.  So, I'm much more pleased with the microformat approach using CSS classes.  And, I'm currently trying to write a general microformat parser using Python's HTMLParser class, which beats using regexes.

Just thought I'd share the revelation, and toot my own fledgling writing horn. :)

[sa]: http://safari.oreilly.com/
[sh]: http://www.oreilly.com/catalog/spiderhks/toc.html
