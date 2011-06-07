--- 
wordpress_id: 810
layout: post
title: On choosing Python for Hacking RSS and Atom
wordpress_url: http://decafbad.com/blog/?p=810
---
<blockquote cite="http://www.annezelenka.com/2005/12/python-slithers-in.html">...I bought this rather interesting book: <a href="http://www.amazon.com/exec/obidos/ASIN/0764597582/0xdecafbad01-20?creative=327641&camp=14573&link_code=as1">Hacking RSS and Atom</a> by Leslie M. Orchard. It covers virtually everything I want to do with my feed blender. Except it does it in Python. Dang.<br /><br />...Programmers seem to get used to the language they use a lot and then find others difficult or poorly designed. As for me, I'm not so excited about Python itself as I am about what I can do with it given a little help from modules like Mark Pilgrim's Universal Feed Parser and Reverend for Bayesian classification.</blockquote>
<small style="text-align:right; display:block">Source: <a href="http://www.annezelenka.com/2005/12/python-slithers-in.html">Anne 2.0: Python Slithers In</a></small>

I've gotten a handful of instances of this sort of feedback about [the book][bo] and my choice of Python for all the code within.  I had anticipated this concern a bit, and hoped it wouldn't be a hurdle for acceptance of the book, but I forged ahead with Python nonetheless.


Some reasons for choosing Python for the book, in no particular order, were:

* The [Universal Feed Parser][ufp] exists.

* Python is one of the cleanest languages I've ever used that still retains a degree of meta-magic.  I'd hoped that this might even help in carrying the notions in the book to other languages, thanks to the clarity of the code.  (Regardless of how clear it actually turned out! :))

* Python is cross-platform enough to work on every machine I use on a regular basis—Windows, Mac, or Linux.  While not omnipresent, it's at least fairly easy to get up and running.

* Python is my current favorite go-to tool.  I'm hoping that this doesn't mean that I've fallen mindlessly into it.  [I'd already forcibly abandoned Perl][perl] to get out of this sort of rut and maintain my flexibility.  (ie. "*Programmers seem to get used to the language they use a lot and then find others difficult or poorly designed.*")
 
Although [my next book][nb] will contain examples in a variety of programming languages, I wonder what language I should lean toward in the future for public-facing purposes?  Lately, I've been [warming up to PHP][php]—how might it have worked for [Hacking RSS and Atom][bo]?

* [MagpieRSS][mp] exists.

* PHP looks like a meta-impaired and jumbled mess to me, compared to Python.  But, it's workable and maybe it's not healthy to be around all that meta all the time.

* PHP is ubiquitous where Python's just starting to get legs on web servers.

* PHP is a lot of others' current favorite go-to tool.

But, I've also been told that it'd be a mistake to run with PHP code listings and that the book would really suffer in clarity.  More thinking to do, but I thought I'd get these thoughts out there at least.

[nb]: http://decafbad.com/blog/2005/12/14/hacking-delicious-is-a-real-book
[perl]: http://decafbad.com/blog/2003/10/16/seeing-out-opposites
[mp]: http://magpierss.sourceforge.net/
[ufp]: http://feedparser.org
[bo]: http://www.amazon.com/exec/obidos/ASIN/0764597582/0xdecafbad01-20?creative=327641&camp=14573&link_code=as1
[php]: http://decafbad.com/blog/2005/12/18/not-so-deep-php-thoughts
