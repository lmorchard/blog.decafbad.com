--- 
wordpress_id: 919
layout: post
title: JavaScript apps with read/write access to S3
wordpress_url: http://decafbad.com/blog/2006/04/03/javascript-apps-with-readwrite-access-to-s3
---
 <p><b>Update:</b> I've started experiments on <a href="http://decafbad.com/trac/wiki/S3Ajax">S3Ajax</a>.</p>
 <p>Notes for my future reference:</p>
     <ul>
     <li>
     <span>There's a <a href="http://pajhome.org.uk/crypt/md5/sha1src.html">SHA1</a> implementation for JavaScript.</span>
     </li>
     <li>
     <span>The <a href="http://developer.amazonwebservices.com/connect/entry.jspa?categoryID=47&externalID=128">authentication scheme for Amazon's S3</a> requires SHA1.</span>
     </li>
     <li>
     <span>JavaScript-based apps can be served up from the S3 domain as files stored via S3.</span>
     </li>
     <li>
     <span>All of this adds up to JavaScript apps hosted on S3 with AJAX-based read/write access to S3 itself.</span>
     </li>
     </ul>
 <p>Also: Imagine GreaseMonkey scripts using S3 as a universal configuration pool and long-term data store.  (The configuration pool idea, by the way, came from Dave Winer.)</p>
