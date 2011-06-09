--- 
wordpress_id: 1380
layout: post
title: Improving my Delicious command for Ubiquity
date: "2008-09-07T01:20:20-04:00"
tags: 
- delicious
- web20
- firefox
- entries
- mozilla
- ubiquity
wordpress_slug: improving-my-delicious-command-for-ubiquity
wordpress_url: http://decafbad.com/blog/?p=1380
---
After writing up my [first stab at a Delicious command for Ubiquity][first], I planned to continue revising it based on feedback and to work on exploring more of what Ubiquity enables.  I started looking into writing my own nouns for tag suggestions, as well as playing with page load and browser startup hooks.  And, I also started poking at a little bit of deeper extension development, which took up most of my time today.

I've [updated my UbiquityCommands][ub] page and checked in my latest revision of [the Delicious command][cmd].  

The main new feature is a status bar item reporting bookmarks for the current page:

<img style="padding: 0.25em" src="http://decafbad.com/2008/ubiq-del-status.jpg" />&nbsp;<img style="padding: 0.25em" src="http://decafbad.com/2008/ubiq-del-tip.jpg" />

As you can see above, the command now comes with a status bar panel powered by the [Delicious URL info JSON feed][urlinfo], providing bookmarking info on every page visited.  It shows a bookmark count, a tooltip with further information, and sends the user to the URL info page on Delicious when clicked.  It mostly works, but it could use some looking at.  This is my first time really cracking open the hood on Firefox and XUL, and so I'm feeling around in the dark.

Specifically, I'm using Ubiquity's page load hook—but I'm also trying to augment that by tracking tab selection events, in order to keep the status bar info updated for the active tab.  But then, that leads me to trying to track new windows, to attach the tab selection event handler for every newly opened window.  Or I could just be barking up the wrong tree entirely.  At any rate, the code is probably brain-dead dumb, so I hope someone can clue me into a better way.

[urlinfo]: http://delicious.com/help/feeds
[cmd]: http://decafbad.com/hgwebdir.cgi/UbiquityCommands/file/tip/delicious.ubiq.js
[ub]: http://decafbad.com/UbiquityCommands/
[first]: http://decafbad.com/blog/2008/09/01/writing-a-delicious-command-for-ubiquity
