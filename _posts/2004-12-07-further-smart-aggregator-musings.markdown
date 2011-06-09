--- 
wordpress_id: 573
layout: post
title: Further musings toward smarter aggregators
excerpt: It seems like the magic Bayesian pixie dust works well for spam-vs-ham in my email box, so why shouldn't the magic for interesting-vs-yawn work for my aggregator firehose?
date: "2004-12-07T16:37:08-05:00"
tags: 
- syndication
wordpress_slug: further-smart-aggregator-musings
wordpress_url: http://www.decafbad.com/blog/?p=573
---
I'm a complete neophyte when it comes to machine learning, but I'd like to get into learning more about the field in general.  In particular, I'd like to make my news aggregator smarter.  I've [already tried using SpamBayes](http://www.decafbad.com/blog/2003/08/16/bayes_agg_one), but that didn't make me happy.  Whether it was my approach or whether it was that Bayes itself is not suited toward this task, I'm not sure, though I suspect it's a little of both.

It seems like the magic Bayesian pixie dust works well for spam-vs-ham in my email box, so why shouldn't the magic for interesting-vs-yawn work for my aggregator firehose?    Well, here are the issues I'm guessing at:

In the case of spam-vs-ham, you want to classify things into this or that-- that which is kept, and that which is tossed away.  But in the case of items in my aggregator, I want a relative sort order or a score.  I want a fuzzy guess toward my interest with which to inform presentation of items.  Interesting-vs-yawn is more of a continuum than a pair of buckets.

And then, there's the passive gathering of behavioral data from my interactions with the aggregator, because I'm sure as hell not going to click ratings or thumbs-up/down all day.  In spam-vs-ham, I could build up two clean mailboxes for training the categorizer, with one containing all spam and the other all ham.  But, in the case of my aggregator, the only thing I'm tracking are items in which I showed interest by revealing more information or by clicking through.  

So, I can say that a particular pile of items are all interesting.  But, my interest level for the rest of the items received is a complete unknown-- maybe I'm vehemently disinterested in those 50 items, but maybe I just never got around to looking at those other 20 and just let them fall off my date range for display.  Thus, I have a pile of ham, and a pile of undifferentiated unknown.  I'm not bothering to provide any cues as to whether I *don't* like something, because that'd be boring work-- I mean, I *am* disinterested in those items, after all.  So, I'd like to leverage what the system knows from what I care to provide, but not jump to any conclusions about the items in the unknown pile.  There is no spam, only various flavors of ham.

Given all this, then, is there anyone out there who knows more about machine learning than me who could maybe point me toward a better approach or algorithm that fits this profile?
<!--more-->
shortname=further_smart_aggregator_musings
