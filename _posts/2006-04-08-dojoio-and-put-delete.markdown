--- 
wordpress_id: 929
layout: post
title: dojo.io and PUT / DELETE
wordpress_url: http://decafbad.com/blog/2006/04/08/dojoio-and-put-delete
---
 <p>Just starting to delve into Dojo for S3Ajax, thanks to <a href="http://decafbad.com/blog/2006/04/06/private-client-side-cookies-for-ajax#comment-9602">the promise of `dojo.storage` for stashing security credentials locally</a>.  And, that <a href="http://dojotoolkit.org/docs/rich_text.html">Rich Text Editor</a> doesn't look shabby either.</p>
 <p>I'm having trouble using `dojo.io`, though.  I'm a little fuzzy on the cross-browser availability of PUT and DELETE methods in XMLHttpRequest objects.  So, I assume that's why `dojo.io` doesn't seem to allow them.</p>
 <p>Code I had working stopped once I swapped over to Dojo's AJAX stuff, which I seemed to root out in the `canHandle` function of `dojo.io.XMLHTTPTransport`.</p>
 <p>So, for now, I'm still rolling my own there.</p>
