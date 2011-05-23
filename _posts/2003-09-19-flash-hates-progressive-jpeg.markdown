--- 
wordpress_id: 480
layout: post
title: Flash MX Hates Progressive JPEGs
wordpress_url: http://www.decafbad.com/blog/?p=480
---
<p>
Okay, I may be the last person fiddling with Flash to
discover this, but here's what I've learned today:
</p>
<p>
<a href="http://www.macromedia.com/support/flash/ts/documents/cant_load_jpg.htm"><b>Flash MX hates progressive JPEGs.</b></a>
</p>
<p>
From the above: "<i>The Macromedia Flash Player does not have a
decompressor for progressive JPEG images, therefore files of this type
cannot be loaded dynamically and will not display when using the
loadMovie action.</i>"
</p>
<p>
This would have been nice to know, hours ago.  Or maybe fixed in
the past year or so since the above linked tech note.  See, although
I'm a Jack of a lot of Trades, I don't really pay attention much
to things like JPEGs and their progressive natures.  It wasn't
until I finally started randomly clicking buttons on and off in
Macromedia Fireworks while exporting a test JPEG that I finally
narrowed down the problem.
</p>
<p>
This was after a day worth of examining ActionScript, XML data,
HTTP headers, and a mess of other random dead ends.  And a lot of
last-ditch random and exhaustive twiddling of checkboxes and
options.
</p>
<p>
<b>Then</b>, once I had the words I
wouldn't have had unless I already knew what my problem was, a Google search for
"<a href="http://www.google.com/search?q=flash+progressive+jpeg&ie=UTF-8&oe=UTF-8">flash progressive jpeg</a>"
got me all kinds of info.
</p>
<p>
Problem is, the JPEGs supplied to the particular Flash app on which
I'm hacking come from a random assortment of people working through
a content management system on the backend.  They upload them
with a form in their browser, and this Flash app gets a URL to the
image via an XML doc it loads.  Me, I'm probably in bed when this
happens.  I'd love to have tested every one... er, rather, no I
wouldn't.
</p>
<p>
So... Now I just have to figure out how to get all these people
to start making sure that their JPEGs aren't progressive.  Hmph.
</p>
<p>
I can only hope that this message gets indexed and maybe provides
more triangulation for some other poor sucker in the future.
</p>
<!--more-->
shortname=flash_hates_progressive_jpeg
