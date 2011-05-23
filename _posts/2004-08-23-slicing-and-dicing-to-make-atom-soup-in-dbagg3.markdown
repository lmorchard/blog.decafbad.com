--- 
wordpress_id: 539
layout: post
title: Slicing and Dicing to Make Atom Soup in dbagg3
excerpt: I've been putting more work into dbagg3, but I'm getting hung up on the database.  Well, actually I'm getting hung up on the subject of XML storage, query, and retrieval in general-- but at present, I'm trying to cram all this data into MySQL and SQLite databases.  But, my tendencies as an abstraction astronaut and my lack of database savvy are tying me (and my data) in knots.  I kept meaning to write a bit Atom (and XML in general) with regard to database storage and query, so maybe now's the time.
wordpress_url: http://www.decafbad.com/blog/?p=539
---
I've been putting more work into [`dbagg3`][dbagg3], but I'm getting hung up on the database.  Well, actually I'm getting hung up on the subject of XML storage, query, and retrieval in general-- but at present, I'm trying to cram all this data into MySQL and SQLite databases.  But, my tendencies as an abstraction astronaut and my lack of database savvy are tying me (and my data) in knots.  I kept meaning to write a bit Atom (and XML in general) with regard to database storage and query, so maybe now's the time.

### XML databases

I'm aware of XML-native databases like [eXist][exist], [Xindice][xindice], and [Berkeley DB XML][bdbxml]-- but I don't want to work in Java right now, and I can't get the Berkeley XML DB compiled and running without segfault under OS X.  This bugs me, though, since the most elegant solution to me is to use something XML-native to store and query piles of Atom feeds and entries.  I'd really like to have [XPath available as a query tool][xpathudell].  And then, though I haven't heard a ton about it lately, there's XQuery.

And, oh yeah, I know there are some commercial solutions (like [Virtuoso][virtuoso]), but umm... no.

### RDF databases

I suppose I could also switch to tossing RDF around internally, maybe use RSS 1.0 under the hood.  This seems to be what the much-similar [Urchin RSS aggregator][urchin] is doing.  (Maybe I should just dump `dbagg3` and pitch in with Urchin.)  But, I don't know the state of RDF art well enough to know whether there's a database available that can handle 10,000 Atom/RSS entries a week or more for a year without gagging.  (My previous database was up to 500,000 entries when I started working on `dbagg3`, and I think that was since last November.)

### SQL databases

So, I'm screwing around with SQL databases-- MySQL and SQLite in particular.  As compared to XML and RDF databases, I know and understand and trust SQL databases so much more with regards to performance and gotchas and general techniques.  

In previous incarnations of my aggregator, MySQL and SQLite served me well with pretty simple data models.  But this time around, I want to play with much richer data: I want to include everything in the Atom spec, and try to take in some metadata from extensions.  So I threw together what I thought was a pretty decent relational model onto which I could map Atom XML data.  (If you're curious, you can check out [a recent schema dump][dbagg3_sql].)

The problem is, with the XML sliced and diced and sprinkled into all these separate tables, it's a **fun** time reassembling the pieces.  I've run into this problem many times before, when trying to map object hierarchies into relational databases, and usually things degrade into nasty self-joins and an explosive number of queries.  This kind of inelegance smells really bad, oily like melting plastic caused by the friction of a square peg being driven into a round hole by my forehead as a hammer.

In the end, what I've usually ended up doing is to forget about mapping from objects to the relational model: tables become a set of indices to objects, the objects themselves packed up as BLOBs via some language-dependant pickling or freezing scheme.  Nasty, ugly, fragile, and completely inelegant.  There's some of that in `dbagg3` *right now*, and I want it out.  Though I used to think it was as clever and neat as a digital watch, this smells even worse than melting plastic.

### XML in SQL databases

My latest thoughts, then, are to accept some bad smells (I *do* like the smell of burning plastic, actually) and simplify my database:  Instead of pickled binary objects, I'll store XML in a column (at least that isn't implementation-tied), and other tables will give me indices to this XML.  Thinking hard about my use cases, I think I can cover 80% of what I need with being able to look things up by feed, by subscription, by user, by date, and a few other useful aspects.  Once I've gotten a pile of data out of the database in XML form, I can then attack it with XSL.

However, what gives me even further enthusiasm for this approach is [this little XPath extension to PostgreSQL][postxml].  This gives you a set of functions to apply XPath to XML-containing columns in SQL queries.  So, you can pull out nodes in a select, or search on the results in a WHERE clause, among other things.  I haven't tried it yet, but it gives me ideas.

One idea is that, through [PySQLite's API additions][pysqliteapi], I can easily add new SQL functions at will-- oh like, say, some XPath functions using libxml2 under python.

Granted, there are no indices backing these XPath searches, and using these python functions added to SQLite comes with overhead, the availability of XPath in SQL could give me the 20% I'm missing with simple tables.  It might be worth the price and the smells.

### So Anyway...

That's where I'm at right now.  I think I've written a bunch, and all this text could use some code examples and some diagrams.  But, I figured I'd think out loud a bit and see if anyone could step in and smack me for being a complete twink.  

I want to slurp in Atom XML data, with arbitrary extensions, and be able to attack it with some reasonable set of queries to recombine this data into new feeds.

I know I'm not the only person thinking about this stuff, and I've got to assume that I'm nowhere near the smartest about it.  I'm still working on this aggregator thing, and making what I think is some fun progress with a [REST interface][dbagg3_api], but this data stuff has me stalled.

So... what do you think?

[virtuoso]: http://virtuoso.openlinksw.com/
[dbagg3_api]: http://www.decafbad.com/cvs/*checkout*/dbagg3/lib/dbagg3/web/api.py?rev=HEAD&#38;content-type=text/x-python
[pysqliteapi]: http://pysqlite.sourceforge.net/old/documentation/pysqlite/node10.html
[postxml]: http://www.throwingbeans.org/tech/postgresql_and_xml.html
[exist]: http://exist.sourceforge.net/
[xindice]: http://xml.apache.org/xindice/
[bdbxml]: http://www.sleepycat.com/products/xml.shtml
[urchin]: http://urchin.sourceforge.net/
[dbagg3]: http://www.decafbad.com/cvs/dbagg3/
[dbagg3_sql]: http://www.decafbad.com/2004/08/dbagg3.sql
[xpathudell]: http://webservices.xml.com/pub/a/ws/2003/04/15/semanticblog.html
