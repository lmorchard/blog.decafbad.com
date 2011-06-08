--- 
wordpress_id: 518
layout: post
title: Feed validation confusion
excerpt: Feed validators are confusing me, but it looks like there's been a fix.
wordpress_slug: feed-validation-confusion
wordpress_date: "2004-05-02T19:27:23-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=518
---
<strike>A bit of feed confusion here:</strike>

* [This validator][validator1] says [my RSS][myrss] is [*valid*][valid].
* <strike>[This validator][validator2] says [my RSS][myrss] is [*invalid*][invalid].</strike>

<strike>Does not compute.  Does not compute.</strike>

**Update:** Hooray!  As mentioned in a [response from Andrew Grumet][andrew], my feed now [validates][invalid].  Thank you!

[myrss]: http://www.decafbad.com/index.rdf
[validator1]:  http://feedvalidator.org/
[validator2]: http://rss.scripting.com/
[valid]: http://feedvalidator.org/check?url=http%3A%2F%2Fwww.decafbad.com%2Findex.rdf
[invalid]: http://rss.scripting.com/?url=http%3A%2F%2Fwww.decafbad.com%2Findex.rdf
[andrew]: http://www.decafbad.com/blog/2004/05/02/feed_validation_confusion#comment-1113
