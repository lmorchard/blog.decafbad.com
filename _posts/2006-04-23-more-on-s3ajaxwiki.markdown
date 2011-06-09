--- 
wordpress_id: 935
layout: post
title: More on S3AjaxWiki
date: "2006-04-23T13:14:54-04:00"
wordpress_slug: more-on-s3ajaxwiki
wordpress_url: http://decafbad.com/blog/2006/04/23/more-on-s3ajaxwiki
---
 <p>So, I've put some more work into <a href="http://s3.amazonaws.com/s3wiki/wiki/StartPage">my S3 AJAX wiki</a>, first mentioned <a href="http://decafbad.com/blog/2006/04/21/an-s3-ajax-wiki">Friday night</a>.  After some Virtual PC sessions, editing seems to be working on Firefox and MSIE on Win.  Safari and any other browsers not amenable to PUT and DELETE in XmlHTTPRequests will not find joy in editing - but the wiki should at least still be navigable and readable since it's plain HTML on the server.</p>
 <p>This thing has certainly not reached any level of stability, but I thought it might be interesting to collect some random thoughts on what good stuff is lurking in there.  So:</p>
     <ul>
     <li>
     <span>One of the mind-bending concepts behind this whole thing for me is that both the documents and the authoring application are all resident on the S3 servers, loaded and run on the fly in a browser.  The magic S3 lends is simple file I/O, taken for granted by applications in nearly every other development environment.  Otherwise, JavaScript in a browser is a very capable system.</span>
     </li>
     <li>
     <span>Of course, since my demo wiki is sitting in an S3 bucket with a public-write ACL, everything's open to vandalism and subversion (of the bad variety)- documents and application both.  S3Ajax does allow authentication through your S3 credentials, though, so a private group with restrictive S3 ACLs could use this wiki successfully.</span>
     </li>
     <li>
     <span>All content managed by the wiki code ends up as HTML on the server.  Maybe some day this will grow up to be proper XHTML.  Using plain old HTML, rather than <a href="http://webseitz.fluxent.com/wiki/SmartAscii">smart ASCII</a>, seems like an important step to me.  HTML is a neutral standard, whereas various wiki formats are far from agreed upon or standardized.  Luckily,  <a href="http://goessner.net/">Stefan G&ouml;ssner's</a> <a href="http://goessner.net/articles/wiky/">Wiky</a> does roundtrip conversion between wiki-text and HTML.</span>
     </li>
     <li>
     <span>Sticking with HTML as the end format also allows me to eventually go beyond wiki text, and on to <a href="http://microformats.org/">microformats</a> like <a href="http://decafbad.com/blog/2005/06/08/greasemonkey-magic">hCalendar</a> and <a href="http://decafbad.com/blog/2006/03/25/about-xoxooutliner">XOXO</a>.  I could even see interchangably using something like <a href="http://dojotoolkit.org/docs/rich_text.html">DOJO's Rich Text Editor</a> as another editing alternative alongside <a href="http://goessner.net/articles/wiky/">Wiky</a>.  Basically, anything that eats and emits HTML can fit into this wiki.</span>
     </li>
     <li>
     <span>One more thought on HTML and the DOM - if you can use HTML as your document format, the browser DOM makes a pretty nice structure and API for the authoring, manipulation, and management of document content.  In this wiki, innerHTML is the main point of document munging.  But, in XoxoOutliner, I do plenty of DOM node shuffling and tweaking.</span>
     </li>
     <li>
     <span>Speaking of innerHTML:  It's not evil, but it seems useful really only when treated as a write-only property.  It's next to useless for serializing the DOM as HTML source.  MSIE and Firefox both offer wildly different results.  So, I wrote <a href="http://decafbad.com/trac/browser/trunk/S3Ajax/js/wiki.js?rev=760#L413"><code>fromDOMtoHTML</code> in wiki.js</a> to take matters into my own hands.  I know MochiKit offers <code>emitHTML</code>, but it doesn't quite do what I want - there are a few odd corner cases I've found myself handling, and I need to filter out all the elements I inject as editing chrome.</span>
     </li>
     <li>
     <span>I like the functional DOM construction kit offered by <a href="http://mochikit.com">MochiKit</a> and <a href="http://www.vivabit.com/bollocks/2006/04/06/introducing-dom-builder">DOM Builder</a> so much that I felt compelled to reinvent my own.  Check out <a href="http://decafbad.com/trac/browser/trunk/S3Ajax/js/common.js?rev=760#L118"><code>createDOM</code> in common.js</a>.  I use it in the <a href="http://decafbad.com/trac/browser/trunk/S3Ajax/js/wiki.js?rev=760#L496"><code>injectEditingFramework</code> function in wiki.js</a> to build and inject all the wiki editing chrome into the page on the fly.  I re-wrote this code so as to not import the bulk of MochiKit, but before I'd heard of DOM Builder.  I'm keeping it around for now.</span>
     </li>
     <li>
     <span>Speaking of reinventing things, check out <a href="http://decafbad.com/trac/browser/trunk/S3Ajax/js/S3Ajax.js?rev=760#L283"><code>xmlToObj</code> in S3Ajax.js</a>.  I hadn't seen <a href="http://badgerfish.ning.com/">BadgerFish</a> until about an hour ago, but <code>xmlToObj</code> is my own simplied version: That is, code to turn XML into basic native JS structures.  I use this to easily deal with the XML response from S3 bucket listings.  It works better than I thought it would.</span>
     </li>
     <li>
     <span>Speaking of <code>xmlToObj</code>, I use an S3 bucket listing with a key prefix to <a href="http://decafbad.com/trac/browser/trunk/S3Ajax/js/wiki.js?rev=760#L259">populate a "recent changes" drop down selector</a>, sorted in reverse chronological order of the LastModified timestamp. </span>
     </li>
     <li>
     <span>And speaking of bucket listings:  I don't use them in finding existing wiki words - but I may do so in a future version.  But, instead, <a href="http://decafbad.com/trac/browser/trunk/S3Ajax/js/wiki.js?rev=760#L118">I got fancy and perform a number of HEAD requests to determine which WikiWords on the page do and don't exist</a>.  I do this with chained AJAX calls - the completion of each fires off the next HEAD until I run out of words to check.  The discovery of non-existent pages linked by wiki word triggers a CSS class change to highlight the word in need of authoring, as well as the attachment of an on-click handler that causes the creation of a new page for that word.</span>
     </li>
     <li>
     <span>In the future, I'd like to use the Atom Publishing Protocol, as well as the OPML Community Server Protocol (<a href="http://decafbad.com/trac/browser/trunk/XoxoOutliner/js/myXMLRPC.js">via XML-RPC</a>).  If any other AJAX-accessible web file systems crop up (GDrive?), I might hit them too.  I'm considering WebDAV, trying to decide if it's worth it.</span>
     </li>
     <li>
     <span>All-in-all, I think where I'm going with this stuff is basically what I wanted to do with <a href="http://decafbad.com/trac/wiki/Micronian">Micronian</a>.</span>
     </li>
     <li>
     <span>OPML is another format I plan to explore with this rig, very soon.</span>
     </li>
     <li>
     <span>I'd love it if someday I could use all of this stuff to research, plan, organize, and write a book.</span>
     </li>
     </ul>
