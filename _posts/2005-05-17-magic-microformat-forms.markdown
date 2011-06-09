--- 
wordpress_id: 644
layout: post
title: Magic Microformat Forms
date: "2005-05-17T12:38:18-04:00"
wordpress_slug: magic-microformat-forms
wordpress_url: http://www.decafbad.com/blog/?p=644
---
<blockquote>What I haven't seen is much discussion about a standard way to encode, upload, or manage microformats, except for Structured Blogging which defines a way to structure blog entries and has a plugin for one blogging application, WordPress. Somehow, I don't think having a plugin for each blogging application that has to implement an editor for each microformat is gonna scale well.</blockquote>
<div align="right"><small>Source: <cite>Ken MacLeod - <a href="http://bitsko.slc.ut.us/blog/2005/05/15#uformat-plugins">Steal this idea: Browser-based microformat plugins</a></cite></small></div>

How about a Greasemonkey script or bookmarklet that will hide a given textarea intended for HTML input, dynamically inserting a form in its place.  This form would contain all the fields necessary to build an hReview, hCalendar, hCard, or whatever flavor of microformat strikes your fancy.  

In the background, the hidden textarea gets populated with a microformatted version of the form's contents via HTML template.  Then, when you're done composing the microformat item, use a magic button or another script/bookmarklet to bring back the original textarea for further editing.

As long as your blogging tool supports posting HTML entries via a textarea in a form, this sort of thing should help facilitate the composition of microformat content.  And hopefully, focusing on the textarea itself can make this sort of thing fairly publishing-tool-agnostic.

Just a quick thought that I haven't time at the moment to implement or check for stupidity.

Of course, this whole idea of [shoehorning structured data into blogs and feeds via specially arranged HTML][shoe] strikes me as similar in spirit to XML-RPC, but it might just [be useful][useful] until something cleaner catches on ([or I catch on to it][catch])...

[catch]: http://www.decafbad.com/blog/2002/11/02/ooocae
[useful]: http://www.decafbad.com/blog/2002/11/26/oooccb
[shoe]: http://www.decafbad.com/blog/2005/05/05/the_right_place_for_data_in_your_feed
