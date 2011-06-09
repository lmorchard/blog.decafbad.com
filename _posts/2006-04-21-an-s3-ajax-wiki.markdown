--- 
wordpress_id: 934
layout: post
title: An S3 AJAX Wiki
date: "2006-04-21T23:52:10-04:00"
wordpress_slug: an-s3-ajax-wiki
wordpress_url: http://decafbad.com/blog/2006/04/21/an-s3-ajax-wiki
---
 <p>So, who knows how long it'll stay up - or if it even works for anyone besides me in Firefox on OS X - but I've got an initial version of an <a href="http://decafbad.com/trac/wiki/S3Ajax">S3Ajax</a>-based wiki:</p>
     <ul>
     <li>
     <span><a href="http://s3.amazonaws.com/s3wiki/wiki/StartPage"><a href="http://s3.amazonaws.com/s3wiki/wiki/StartPage">http://s3.amazonaws.com/s3wiki/wiki/StartPage</a></a></span>
     </li>
     </ul>
 <p>I'm using <a href="http://goessner.net/">Stefan G&ouml;ssner's</a> <a href="http://goessner.net/articles/wiky/">Wiky</a>, to handle round trip conversion between wiki text and HTML.  My <a href="http://decafbad.com/trac/wiki/S3Ajax">S3Ajax</a> handles all the I/O, tied together with a clunky <a href="http://s3.amazonaws.com/s3wiki/js/wiki.js">wiki.js</a>.</p>
 <p>I've not had time yet to test this at all, but I figured setting it loose on a public-write ACL bucket on S3 would surely get bugs exposed.  :) Be aware that I will nuke this bucket for any whimisical reason, including porn or spam or excessive usage costs.</p>
 <p>Anyway, one of the main tricks to this thing of which I'm particularly enamoured is the fact that all the pages are stored as HTML.  There's a bit of JS and CSS include hell going on in the page header that I'd like to reduce, but all the wiki text mungeing happens in the browser.  What lands in the S3 bucket is pure HTML, fully able to be separated from the wiki system and crawled by Google or processed in whatever other way you'd like.</p>
 <p>More soon.  For now:  I go to bed.</p>
