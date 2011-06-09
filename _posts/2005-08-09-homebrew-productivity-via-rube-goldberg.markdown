--- 
wordpress_id: 673
layout: post
title: Homebrew Productivity via Rube Goldberg
date: "2005-08-09T09:59:00-04:00"
wordpress_slug: homebrew-productivity-via-rube-goldberg
wordpress_url: http://www.decafbad.com/blog/?p=673
---
Here's a quick weekend assemblage of a hack that might be of use to someone:

I recently switched to a [Palm Zire][zire] from a Handspring Visor--which itself was [a downgrade from a Treo 600][down].  The Zire was a bit of a lateral move from the Visor, since the Zire is rechargeable and more pocketable, but has less storage and a screen with tinier eye-strainy pixels.  (Actually, the product page I linked here shows the Zire 21, whereas what I have is the discontinued classic Zire.)

Anyway, I've been idly poking at making this thing more useful as my take-along brain bucket.  The out-of-box tools--Palm Desktop, etal--have never quite worked for me, so I wanted to see what might *actually* help me get some use out of the thing.  So far, it turns out that it ends up being most convenient when I use it as a glorified electronic notepad, a [Hipster PDA][hipster] with a USB socket.

I've thrown together a combination of [MacNoteTaker][notetaker], [Markdown][markdown],  [Remind][remind], [Dasher][dasher], and [ShellWatcher][shellwatcher] to implement my own idea-dump and to-do conduits into my PowerBook.  

The nice thing about [MacNoteTaker][notetaker] is that it simply syncs text files.  From there, it's easy to route things through [Markdown][markdown] and [Remind][remind].  

I was using [Nick Vargish's Remind Widget][remind_widget] before [my hard drive crash][crash], but since then the download seems to have gone AWOL.  So, [ShellWatcher][shellwatcher] it is, running `~/local/bin/remind` to update my Dashboard reminders on a regular basis.  To keep these reminders in my face throughout the day, I've got [Dasher][dasher] set to bring the Dashboard up whenever I walk away for more than 5 minutes.

As for plain old ideas, I've got a `00-random.txt` file I maintain between the PowerBook and [MacNoteTaker][notetaker].  This is in [Markdown][markdown] format, and I occasionally view it via a filter CGI in my browser.  I'm considering plastering it up on my Dashboard via a browser-refresh widget also.  Eventually, these ideas migrate into [Tinderbox][tinderbox] or a personal wiki.

For my next productivity micro-project, I'm thinking of setting up an email gateway to let my fianc&#233;e email me honey-do lists that'll get merged in with my reminders...

[tinderbox]: http://www.eastgate.com/Tinderbox/
[dasher]: http://www.splasm.com/products/productdasher.html
[remind]: http://www.roaringpenguin.com/penguin/open_source_remind.php
[shellwatcher]: http://www.apple.com/downloads/dashboard/developer/shellwatcher.html
[remind_widget]: http://www.43folders.com/2005/06/dashboard_widge.html
[down]: http://www.decafbad.com/blog/2005/06/14/gadget_flashback
[notetaker]: http://homepage.mac.com/wis/Personal/programs/NoteTaker/NoteTaker.html
[hipster]: http://www.hipsterpda.com/
[zire]: http://www.palm.com/us/products/zire/
[markdown]: http://daringfireball.net/projects/markdown/
[crash]: http://www.decafbad.com/blog/2005/07/05/exocortex_stroke
