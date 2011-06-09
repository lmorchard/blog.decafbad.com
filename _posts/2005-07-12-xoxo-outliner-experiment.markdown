--- 
wordpress_id: 667
layout: post
title: In-browser XOXO Outliner Experiment
date: "2005-07-12T17:56:34-04:00"
wordpress_slug: xoxo-outliner-experiment
wordpress_url: http://www.decafbad.com/blog/?p=667
---
Testing, testing--is this thing on?  Well, I do have to say that I've recovered rather well from [the "stroke"][stroke] last week.  Things have been pretty busy since then, so I haven't had much of a chance to blather any more around these parts.

However, in the spirit of a few [recent][graphs] [experiments][treemaps], I have another demo for you.  Here's the URL of the latest work in progress / proof of concept:

* [http://www.decafbad.com/2005/07/map-test/tree2.html](http://www.decafbad.com/2005/07/map-test/tree2.html)

What is it, you might ask before clicking a strange URL?  It's an outliner, in Javascript.  Or, rather, a first rough stab at one anyway.  It's got a long way to go, and there are indeed [better options out there already][sprout], but I wanted to try making one myself.

A quick summary of controls:  No mouse drag of items yet, but you can click on them to edit.  Use the up and down cursor keys to navigate through the outline.  Use shift along with the cursor keys to *shift* items around.  Use the control key along with the cursor keys to *control* visibility of child items.

*Update*: There're a few more things I didn't mention, as well as a few bug half-fixes.  Hitting return when the editor is on an existing item will insert a new blank item right after it.  Hitting shift-return will append a new child item to the current item.  Tab and shift-tab, as well as shift-right and shift-left, are supposed to indent and outdent items.  Unfortunately, they're not quite working yet and of course they semi-clobber other useful keyboard functions, so I'm still feeling around for a good way to support these.

The idea is that I want to unobtrusively drop some CSS and JavaScript into an HTML page with one or more [XOXO-style outlines][xoxo], magically turning them into in-browser outline editors.

But, like I said, there's still lots of work to be done here, and I'm pretty sure I've riddled this thing with circular references that will make your [IE/Win combination leak like crazy][leak].  I just wanted to see if I could make something like this work, though.  And, roughly, it seems to do so in Safari and Firefox.

The next part of this equation will be coming up soon, I think.  And that is: Okay, now that I've created / edited an outline in my browser--how can I save it?  

[leak]: http://jibbering.com/faq/faq_notes/closures.html#clMem
[xoxo]: http://developers.technorati.com/wiki/XOXO
[sprout]: http://www.google.com/url?sa=U&start=1&q=http://sproutliner.com/&e=912
[stroke]: http://www.decafbad.com/blog/2005/07/05/exocortex_stroke
[treemaps]: http://www.decafbad.com/blog/2005/07/02/css_treemaps
[graphs]: http://www.decafbad.com/blog/2005/07/02/drag_the_boxes_stretch_the_lines
<!--more-->
shortname=xoxo_outliner_experiment
