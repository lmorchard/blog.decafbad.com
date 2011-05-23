--- 
wordpress_id: 949
layout: post
title: Back to NewsRiver, and hacking lists of Reading Lists
wordpress_url: http://decafbad.com/blog/2006/05/12/back-to-newsriver-and-hacking-lists-of-reading-lists
---
 <p>After a bit of a hiatus from it, I'm again back to using <a href="http://www.newsriver.org">NewsRiver</a> (with <a href="http://decafbad.com/trac/wiki/DecafbadNewsRiver">my own modifications</a>) as my primary feed reader.  NetNewsWire was starting to feel stagnant to me again, and my only real gripe with NewsRiver was that it seemed to be choking on an unknown few of my feeds.</p>
 <p>So, I took this opportunity to do a little subscription list spring cleaning.  You see, I've been maintaining pretty much the same growing list of subscriptions since around 2002 when I first started playing with Radio UserLand.  It's since followed me around, though export and import and conversion and various other transformations.</p>
 <p>This time, it came out of NetNewsWire and went into the OPML editor.  I opened a <a href="http://hosting.opml.org/decafbad/subscriptions.opml">fresh OPML file</a> and started creating new categories.  I'd initially thought of using my top del.icio.us tags as a starting point for my new feed subdivisions - but that seemed not quite to work.</p>
 <p>The second thing I ran into is that NewsRiver wants reading lists as individual OPML files whose contents consist of a flat list of outline nodes - no hierarchy or sub-branches.  However, I'd tried maintaining things like that during my last round of NewsRiver usage, and it frustrated the crap out of me.  No, maintaining all my subscriptions in a single OPML file, arranged by overall personal topic, is the way for me.</p>
 <p>How to get these reading lists into NewsRiver, then, without breaking them up into separate files?  Well...  NewsRIver doesn't need separate files, per se, just separate URLs.  So, <a href="http://hosting.opml.org/decafbad/reading-list-tools.xsl">XSL to the rescue</a>. I wrote a quick URL-line tool in PHP to transform the OPML using this XSL, which gives me this:</p>
     <ul>
     <li>
     <span><a href="http://decafbad.com/2006/05/xsltproc.php?mode=toc&suboutline=amusements&xml=http://hosting.opml.org/decafbad/subscriptions.opml&xsl=http://hosting.opml.org/decafbad/reading-list-tools.xsl">subscriptions.opml - available reading lists</a></span>
     </li>
     </ul>
 <p>Notice that that link above leads to an HTML page, offering a list of links to individual OPML reading lists.  Click on one - if you're running one of my favorite browsers, you'll see what still seems to be an HTML page listing feeds.  In reality, that's in OPML.  View source to see the trick at work.</p>
 <p>In any case, each of those OPML links have worked just fine for me as subscriptions in NewsRiver.  And, I get to manage the whole shebang in one bit OPML outline while still getting my <a href="http://decafbad.com/blog/2006/01/01/new-feed-reader-ideas-for-the-new-year">stratified River of News</a> I've been wanting.</p>
 <p>I keep thinking that I might like to follow up my in-progress <a href="http://decafbad.com/trac/wiki/FeedMagick">FeedMagick</a> tool with some sort of "OutlineMagick" package.  Who knows - maybe this one-off project will be the start of something like that.</p>
