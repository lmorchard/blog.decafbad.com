--- 
wordpress_id: 669
layout: post
title: AJAX Testing and Logging
date: "2005-07-18T14:28:19-04:00"
wordpress_slug: ajax-testing-and-logging
wordpress_url: http://www.decafbad.com/blog/?p=669
---
Okay, okay, I'll admit it: I'm an [architecture astronaut][aa].  I'd join Architecture Astronauts Anonymous--but that'd be AAA, and we already use them for our car insurance. Anyway, here's my current trip into orbit:

[aa]: http://www.joelonsoftware.com/articles/fog0000000018.html

* [http://www.decafbad.com/2005/07/xmlwiki/www/tests.html](http://www.decafbad.com/2005/07/xmlwiki/www/tests.html)

If you click on that, you should see a page with a large textarea appear, in which a running log of tests begins.  So far, all but two of the tests succeed for me in Safari, FireFox, and MSIE6.  I've got a bit more work to do on writing tests, though, as well as working on the server side.

But, there are things going on behind the scenes in this test harness that I want to share right now before I fly off into space.

## Testing with AJAX

First off, about a week ago, I mentioned an [experiment in REST and XML][exp] with which I was starting to play.  In a nutshell, it's a bastard hybrid between a wiki and an XML database, with a REST API.  Well, at the time, I was just poking at it with [invocations of cURL from the command line][curl].  

But, my eventual goal was to get this thing hooked up with a browser via XMLHttpRequests and JavaScript.  Before just flying off to [wire up any UI demos][outliner], though, I wanted to run it through some repeatable tests.  So first, I made my own XmlHTTPRequest wrapper:

* [http://www.decafbad.com/2005/07/xmlwiki/www/js/httpclient.js](http://www.decafbad.com/2005/07/xmlwiki/www/js/httpclient.js)

Then, I went in search of unit testing frameworks for in-browser JavaScript.  I found a few neat things--including [JsUnit](http://www.edwardh.com/jsunit/), [Selenium][selenium], and [httpunit](http://httpunit.sourceforge.net/).

But, none of these quite fulfilled my requirements of a) being simple, b) working well with code continuity broken by asynchronous HTTP requests, and c) being learned by me in an impatient jiffy.  So, I made this:

* [http://www.decafbad.com/2005/07/xmlwiki/www/js/tests.js](http://www.decafbad.com/2005/07/xmlwiki/www/js/tests.js)

It's by no means general or even all that nice to look at, but I've got half a mind to further refactor this into my own AJAX-friendly mini-rendition of [JUnit][junit].  To anyone out there: Let me know if this would be useful, or if I'm just wasting my time.

[junit]: http://www.junit.org/index.htm
[outliner]: http://www.decafbad.com/blog/2005/07/12/xoxo_outliner_experiment
[curl]: http://www.decafbad.com/2005/07/xmlwiki/doc/log.txt
[exp]: http://www.decafbad.com/blog/2005/07/12/an_experiment_in_rest_and_xml
[selenium]: http://selenium.thoughtworks.com/index.html

## Logging in Browser-based JavaScript

Along the way through reinventing my own testing wheel, I also got fed up with the usual ways I was used to generating debugging and informative messages from my JavaScript code.  So, I went off in search for something like [Log4J][log4j] in Java or the [logging][logging] module in Python.

The closest I came was to `selenium-logging.js` in the [Selenium][selenium] package, but that wasn't really what I wanted.  So, I made this:

* [http://www.decafbad.com/2005/07/xmlwiki/www/js/log.js](http://www.decafbad.com/2005/07/xmlwiki/www/js/log.js)

It's by no means general or even all that nice to look at, but I've got half a mind to further expand this into my own JavaScript mini-rendition of [logging][logging].  Imagine logging from a browser-based JavaScript app to a server-based REST-ified syslog.  Seems like it *could* be useful, if done right.  To anyone out there: Let me know if this would be useful, or if I'm just wasting my time.

[log4j]: http://logging.apache.org/log4j/docs/
[logging]: http://www.python.org/doc/current/lib/module-logging.html

## But wait, there's more...

I'll break off here and continue in another post with [the server-side things I started doing with WSGI][next].

[next]: http://www.decafbad.com/blog/2005/07/18/discovering_wsgi_and_xslt_as_middleware
