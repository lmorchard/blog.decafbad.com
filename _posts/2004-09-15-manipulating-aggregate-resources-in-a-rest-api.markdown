--- 
wordpress_id: 547
layout: post
title: Manipulating aggregate resources in a REST API?
excerpt: So... am I missing a more elegant RESTful way of doing this which doesn't result in a quadrillion HTTP requests?
tags: 
- xml
wordpress_slug: manipulating-aggregate-resources-in-a-rest-api
wordpress_date: "2004-09-15T14:48:53-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=547
---
Here's a tiny bit of a REST-ian quandary:  I'm working through this API for `dbagg3`.  The major resources involved include **subscriptions** and **entries**.  Quite often, while working on the UI, I find a need to manipulate ranges and collections of these resources-- things like: &#8220;mark these 12 entries as read&#8221; and &#8220;give me an aggregate of the new entries for these 6 subscriptions&#8221;.

So, I have been using URLs like the following:

* `POST /subscriptions/523/entries/12322,12326,12325,12388,12412/notes/`
* `GET /subscriptions/312,443,523/now-12.xml`

Doing things this way is terribly convenient with regard to stuffing many things into one HTTP request.  Problem is, with respect to REST, these URLs no longer refer to individual resources--  they're aggregate references.

I've been thinking about this apparent break with the REST philosophy, and was reminded of it after skimming through [Mark Baker's notes on a talk][mbakerrest] today.  

So... am I missing a more elegant RESTful way of doing this which doesn't result in a quadrillion HTTP requests?

[mbakerrest]: http://www.markbaker.ca/Talks/2004-xmlself/all.htm
