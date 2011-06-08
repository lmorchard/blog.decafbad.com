--- 
wordpress_id: 495
layout: post
title: Microcontent and RSS-Data
wordpress_slug: microcontent-and-rss-data
wordpress_date: "2003-10-08T08:30:52-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=495
---
<p>
In response to the opposition to RSS-Data,
<a href="http://blogs.it/0100198/2003/10/07.html#a1818">Marc asks</a>,
"Where are the Reviews, Resumes, Recipes, Topics and other cool new
forms of micro-content?"
</p>
<p>
Well, I did a bit of Googling this morning, and this is what I found:
</p>
<ul>
<li>
On the subject of reviews, A.M. Kuchling
<a href="http://www.amk.ca/xml/reviews.html">has provided</a> an
<a href="http://amk.ca/xml/review/1.0">RDF namespace</a>
for embedding book review metadata within XHTML documents.
</li>
<li>
For resumes,
Uldis Bojars
<a href="http://lists.w3.org/Archives/Public/www-rdf-interest/2002Jun/0077.html">has been working</a> on an
<a href="http://nightman.lv/~captsolo/cv.rdfs">RDF schema for resumes and CV</a>.
</li>
<li>
To offer up recipes, I found
<a href="http://donnafales.com/2002/07/28/recipe-schema">this RDF schema</a>
for <a href="http://donnafales.com/2003/recipes">recipes</a> hosted on
<a href="http://donnafales.com">donnafales.com</a>.
</li>
<li>
As for topics, well, there's already a straight RSS 2.0 namespace
extension called <a href="http://matt.blogs.it/specs/ENT/1.0/">Easy News Topics</a>.
</li>
<li>
And, finally, for events there is
<a href="http://web.resource.org/rss/1.0/modules/event/">mod_event</a>,
and RSS 1.0 module used for presenting calendar event information.
</li>
</ul>
<p>
Yes, with the exception of ENT, these are RDF schema or namespaces.
But, any one of them could likely be adapted to straight XML and used as an RSS 2.0
namespace, thereby leveraging the work these people have already done
in modeling these kinds of content, as well as potentially providing
an easy transformation path to RDF for those who care.
</p>
<p>
What does RSS-Data provide out of the box which makes any of the
above obsolete?  There's no magic here, other than translating between
raw data sctructures.  You'll still need to do the same sort of
modeling and structure work that the authors of all the above have
done.  It's always nicer to have someone else do homework for you.
</p>
<p>
So, if all this new microcontent is so hot, why hasn't anything like
the above been put into use?  Would adding 5 new tags to an RSS
feed really be an insane burden to express calendar events?  Granted,
some of the other examples above are more complex, but then so are
the things they seek to represent.
</p>
<p>
What's the RSS-Data magic that improves on all the above?
</p>
<!--more-->
shortname=microcontent_and_rss_data
