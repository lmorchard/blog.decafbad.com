--- 
wordpress_id: 586
layout: post
title: The Blogosphere as a Tuple Space
excerpt: These tuple spaces seem pretty nifty.  I wonder how we can make the web more like a tuple space?
wordpress_slug: the-blogosphere-as-a-tuple-space
wordpress_date: "2005-01-12T16:12:40-05:00"
wordpress_url: http://www.decafbad.com/blog/?p=586
---
It just occurred to me today that the blogosphere is like a [Tuple Space][tuples].  Or rather, each person's light cone in the blogosphere, made up of the feeds and blogs you track and what you publish, is a [Tuple Space][tuples]--and the blogosphere itself is the union of every personal [Tuple Space][tuples] in existence.

What's a Tuple Space?
---------------------

In case you're not at all familiar with [Tuple Spaces][tuples], this is how I understand them:  

There's a magic bag full of marbles.  The marbles have all sorts of different properties, like color, roundness, size, and material.  You can put in marbles of any sort, and so can everyone else.  When you want to take marbles out, you tell the bag what you want.  

For instance, "Bag, I want blue marbles made of glass," and you'll get a pile of marbles that are blue and made of glass, but come in all sizes and degrees of roundness.  Someone else asks for 1cm-wide egg-shaped marbles made of high-bounce rubber, they get egg-shaped bouncing marbles in all kinds of colors.

Now, real [Tuple Spaces][tuples] are even more abstract than this.  Python has tuples; they look something like this:

    ("foo", 1, 2, "baz", 23.2)
    (4, 5, 6)
    ("foo", 7, 2, "xyzzy", 89)
    ("foo", 9, 2, "xyzzy", 100.3)
    (ExampleObject("wheee"), 123, None)
    (23,)
    
Imagine the magic bag is a heap of these tuples.  You ask for tuples by *pattern*, like this:

    ("foo", ?int, 2, ?str, ?float)
    
And the bag would give you the tuples which match the pattern:

    ("foo", 1, 2, "baz", 23.2)
    ("foo", 9, 2, "xyzzy", 100.3)

The thing that makes this even more abstract than a bag of marbles is that these tuples are just ordered collections of data items.  They're not labeled as properties like "color", "size", "shape", or "material".  Where the data items within tuples pick up meaning is through agreement amongst users of the tuple space.  

Tuple spaces get really interesting, though, because different collectives of users of the tuple space can each agree upon different sets of meanings for tuples--and the agreements exist outside of tuple space, so the space doesn't need reconfiguration for any particular new use.  Meanwhile, the infrastructure supporting the sharing of the tuple space remains simple, and the interface remains the same.  Because they don't know any better, tuple spaces can allow for all kinds of sharing and coordination that no one necessarily has to plan for ahead of time.

For example, want to send instant messages?  Fill space with tuples like this:

    ("TIM-Msg", "Joe", "Frank", "2004-01-12T15:49:00", "Hi there, Joe.")
    ("TIM-Msg", "Frank", "Joe", "2004-01-12T15:52:00", "Hey Frank, how's it going?")
    ("TIM-Msg", "Joe", "Frank", "2004-01-12T16:01:00", "Good, good.")
    ("TIM-Msg", "Frank", "Joe", "2004-01-12T16:12:00", "Glad to hear it!")
    
You can probably figure out what meanings the "TupleIM" client would assign to tuple elements.  If you were Joe, your client might leave a running query in space for tuples like `("TIM-Msg", "Joe", ?, ?, ?)`, where as Frank would subscribe to a query like `("TIM-Msg", "Frank", ?, ?, ?)` .  

What Do Tuples Have to Do with Blogs?
-------------------------------------

Well, we're not really there yet, but the parallels between blogs, the web, REST APIs, and tuple spaces are many.  The web sounds an awful lot like a potential tuple space to me, although it needs a lot of work to become one.  Resources accessible by URL are kind of like tuples, though Google doesn't make quite as universal a tuple-finder as we'd like.  Syndication feeds, however, and the metadata they carry causes the data items to be better exposed to a potential tuple-finder.

But, think about the [Lazyweb][lazyweb].  Want something made?  Post a description of it on your blog and trackback to the [Lazyweb][lazyweb].  (Put a marble in the bag, insert a tuple into space.)  Bored and want to make something?  Subscribe to the [Lazyweb][lazyweb] feed and watch for interesting projects to roll by.  (Ask the bag for fun marbles, search for special tuples.)  The person who posted the project might have never met the person who eventually implements the project, but the blogosphere enabled the interaction.  The people involved took on at least half of the duty in finding tuples, but there seem to be tuple-space-esque things going on here.

Ever post something to your blog with no specific set of people in mind?  Maybe just a vague notion of what *sort* of people might want to read it or respond to you?  Ever get surprised by who responds to your postings?  

That feels like a tuple space to me.  

These tuple spaces seem pretty nifty.  I wonder how we can make the web more like a tuple space?

[lazyweb]: http://www.lazyweb.org/
[tuples]: http://c2.com/cgi/wiki?TupleSpace
