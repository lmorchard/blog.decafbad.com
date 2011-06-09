--- 
wordpress_id: 790
layout: post
title: RSS plumbing in PHP nowhere to be found?
date: "2005-12-09T01:45:30-05:00"
tags: 
- asides
wordpress_slug: rss-plumbing-in-php-nowhere-to-be-found
wordpress_url: http://decafbad.com/blog/?p=790
---
This actually surprises me:  I can't find any simple RSS filters—or other basic feed plumbing fixtures—implemented in PHP.  

I want a [URL-line style][ul] PHP page which takes in an RSS feed URL and some search parameters, returning an RSS feed filtered according to the parameters.  So, say, I want to filter a feed for only items containing a certain phrase in the description—or maybe I want items with `osx` in a `dc:subject` element.

And how about some blenders?  That is, I pass in any number of feed URLs and get one merged feed out the other end.  I've got a chapter in my book on these, in Python—but it'd be handy to have them in PHP as well.

Have I just not looked hard enough?  By now, I'd've thought this sort of thing would be all tied up in a bow and at the top of the Google charts by now.  It makes me wish I'd used PHP in my book, rather than Python—and only because of PHP's irresistible ubiquity.  Coding in PHP still makes me gag, just a bit.

But, if the lazy web doesn't deliver, I guess I'll be cobbling it together myself soon.

[ul]: http://207.22.26.166/bytecols/2001-08-15.html
