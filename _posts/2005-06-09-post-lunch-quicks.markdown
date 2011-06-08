--- 
wordpress_id: 648
layout: post
title: Post-Lunch Quicks
wordpress_slug: post-lunch-quicks
wordpress_date: "2005-06-09T14:06:08-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=648
---
* The [BBS Documentary][bbs] rocks, and it needs to be running on something like PBS.  Although I can understand many people will balk at the $50, it's really rather under-priced.

* I wish the Activity Monitor on OS X Tiger allowed you to [renice][] processes.  I wonder if there's something QuickSilver could do about this?  Like renice the foreground app, or renice a selected app as a second-pane verb?

* There's a utility I use from the shell on OS X that thankfully still works on Tiger.  I found it hidden in [Proteron MaxMenus][mm], [via an macosxhints hint][drg] I read a few years ago.

  In a nutshell, it initiates drag-and-drop from the shell.  I type this:
  
  `drg some_random_podcast.mp3`

  And, in a few seconds, a ghostly icon of the file appears under my mouse, ready to be dragged into iTunes.  

  Funny thing is, I've never actually used MaxMenus much, having gone the route of LaunchBar and QuickSilver for task accelleration.  But, this little utility binary is hidden under the following long-winded path when MaxMenus is installed for the current user:

    `~/Library/PreferencePanes/MaxMenus.prefPane/
     Contents/Resources/MaxMenus.app/Contents/Resources/ MarsNeedsWomen`

  I suppose I could get into the habit of using QuickSilver from the command line for a more flexible and integrated experience.  Or, I could check out the shareware [CLIDrag][cli].  But, this is just a habit I've had since I first switched to Mac after the release of OS X, and I've been careful to keep this binary backed up through the half-dozen or so complete reinstallations I've done since then.

[cli]: http://www.ittpoi.com/drag/
[mm]: http://www.proteron.com/maxmenus/
[drg]: http://www.macosxhints.com/article.php?story=20021220062633569

[renice]: http://www.osxfaq.com/man/8/renice.ws
[bbs]: http://www.bbsdocumentary.com/order/
