--- 
wordpress_id: 863
layout: post
title: Further work on decafbadNewsRiver
wordpress_url: http://decafbad.com/blog/?p=863
---
So, when I need breaks from <a href="http://decafbad.com/blog/2005/12/14/hacking-delicious-is-a-real-book">the book</a>, I've been poking around at <a href="http://www.newsriver.org/">NewsRiver</a> customizations in <a href="http://hosting.opml.org/decafbad/decafbadNewsRiver/decafbadNewsRiver.root">decafbadNewsRiver.root</a> for "fun" programming.  You can check out the <a href="http://hosting.opml.org/decafbad/decafbadNewsRiver/decafbadNewsRiver-relnotes.opml">Release Notes</a> I have so far, but here are a few highlights:

* News items can be filtered by Reading List, and a "Further Reading" list of links to view by filter are displayed at the end of the page after all the news.
* I've split just about all the HTML out of the news rendering code into separate templates, for the start of a switchable theme system.  These themes can be somewhat self-contained, allowing you to make extensive changes to how the news items are presented, without needing to dig into the core suite of code.
* I stole preferences code from NewsRiver itself to facilitate selecting a theme.  It's actually quite slick and nice to work with.
* The first theme is based on the aggregator UI I've been working on since my <a href="http://www.decafbad.com/twiki/bin/view/Main/AmphetaOutlines">AmphetaOutlines</a> days, running up through my <a href="http://decafbad.com/blog/2005/10/05/feedspool-is-progressing-nicely">miniagg</a> implementation.  Check out <a href="http://www.decafbad.com/blog_attachments/miniagg-1.jpg">a screenshot</a> of miniagg - that's pretty much how decafbadNewsRiver looks right now.

Lots and lots of bugs, miles and miles away from any sort of release I want to make, but it's been neat poking at this UserTalk stuff again, even with the usual creaks and ancient lizard brain corners I've run into.  I daresay that, while UserTalk and the whole stack isn't as nice to me as Python, it's quite a bit more satisfying than PHP.
