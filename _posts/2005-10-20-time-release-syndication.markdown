--- 
wordpress_id: 740
layout: post
title: Time-release Syndication
wordpress_url: http://decafbad.com/blog/?p=740
---
<blockquote cite="http://www.surfarama.com/index.php?p=242">Want to read Cory Doctorow’s new book, Someone comes to Town, Someone leaves Town, via RSS?<br /><br />This chicklet will let you do just that…doesn’t matter when you first subscribe, this feed will deliver the book to your feed reader in the right order, a couple of chapters a day, over the next month. You could even subscribe via WINKsite and get it all on your mobile phone…</blockquote>
<small style="text-align:right; display:block">Source: <a href="http://www.surfarama.com/index.php?p=242">Surfarama » RSS for serialized content</a></small>

I've been toying around with a few ideas for something like this for a few years, but have never bothered to finish any of them.  [Russell Beattie][rb] had an interesting implementation of this too.

But, just in case I never actually *do* anything with this notion, here's a free idea—I wonder how many aggregators actually obey a `301 Moved Permanently` HTTP status code?  

[Simon Willison wrote about this notion][sw]: A reader subscribes using a clean and simple feed URL, but the aggregator receives a `301` redirect upon the first `GET`.  This redirect shifts the subscription over to a new feed URL with a unique ID for the reader, thereby uniquely tagging every new subscription to the feed.  The aggregator should then continue to use this tagged URL for all future requests.

However, tagging a subscriber with an RSS radio collar implies that you'll have a database on the server maintaining notes tied to those IDs.  That might be cool if I'm trying to gather some metrics, but for simple time-release syndication I don't really care about tracking a *person*.  I want to track a *start time*.  

What if this post-redirect feed URL had the time of initial redirect in it, and the time release was just a function of the duration since that initial redirect?  Anonymous and no need for a database.  My notion is that I'll just need a PHP script and a fully-formed "master feed" on which the time-release feed will be a time-bounded "viewport" informed by a little date math.  

Or, maybe I'll have a pile of pre-prepared content in a folder and munge that into a feed.  Imagine a podcast like [Scott Sigler's Ancestor][anc], all queued up and ready on the server, but doled out automatically on a weekly basis from the beginning from the point you subscribed.  I'll leave as exercises for the reader issues of "obfuscating" URLs so that people can't easily skip ahead through the story.

<!-- tags: rss atom syndication rest http podcasting -->

[anc]: http://www.project-daemon.net/
[sw]: http://simon.incutio.com/archive/2004/09/01/track
[rb]: http://www.russellbeattie.com/notebook/1008220.html
