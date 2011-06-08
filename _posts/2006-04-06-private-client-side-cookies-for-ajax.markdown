--- 
wordpress_id: 925
layout: post
title: Private client-side cookies for AJAX?
tags: 
- asides
wordpress_slug: private-client-side-cookies-for-ajax
wordpress_date: "2006-04-06T09:46:38-04:00"
wordpress_url: http://decafbad.com/blog/2006/04/06/private-client-side-cookies-for-ajax
---
 <p>Along with the S3 stuff I'm poking at in AJAX, I'd like to retain the user's key ID and secret for S3 locally so that it doesn't need to be reentered all the time or stuck into constants on a server-held file.  But, I don't want to stick it into cookies or anything that will go over the wire - since the whole point of the HMAC authentication is to prevent that from happening.</p>
 <p>I've looked at <a href="http://codinginparadise.org/projects/storage/README.html">AMASS</a>, but it appears to be broken on Mac - which is a non-starter for me on my PowerBook.  I'm wondering if there's any other practical way to retain a pair of strings locally across browsers for an AJAX app.  Because, beyond just that bit of local storage requirement, I've got entire vistas of persistence available on S3.</p>
 <p>I suppose I could stick the credentials in a cookie, then further encrypt them with a friendlier username / passphrase.  The main issue I see with constantly reentering the credentials is that they're these big honking strings that I'll never be able to remember like a username and password.</p>
