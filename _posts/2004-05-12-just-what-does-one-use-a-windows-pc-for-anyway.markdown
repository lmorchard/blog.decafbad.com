--- 
wordpress_id: 522
layout: post
title: Just what does one use a Windows PC for anyway?
excerpt: Wherein I try making a Windows box do things it's probably not supposed to do, and am frustrated when it doesn't quite do what I want it to do.
wordpress_url: http://www.decafbad.com/blog/?p=522
---
Huh.  Having just read [Jeremy Zawodny's account][account] of how easy it was for him to move everything over from one PowerBook to another, and wondering if Windows would ever offer that ease, has me wondering why I bothered to re-install WinXP on my aging desktop PC.  Not quite the same thing, but it's making me appreciate the Windows-free life we've been living at home here.

I had been running Debian Linux on the box, and it mostly served as a file server and a workbench for various experiments.  Well, I got the bright idea that I might be able to get most of the same benefits, and get my [TV capturing][tv] working again, by reverting to WinXP along with an installation of [coLinux][colinux] and / or [Cygwin][cygwin].  Oh yeah, and I'd be able to play a few [old games][subspace] I'd [been missing][ut] too!  Also, I keep meaning to play with the .Net framework and Virtual PC on my PowerBook just hasn't worked out so well.

Well, the first thing I bumped into was that the big drive I was using for file serving was formatted as ext2.  Not really a good option for WinXP.

So, I started playing with [coLinux][colinux] with some interesting results.  Managed to get it up and running with a [Gentoo Linux][gentoo] image, and then I discovered that [coLinux][colinux] could mount the ext2 partition directly from the WinXP device path.  One installation of Samba later, and I was mounting the ext2 partition under Windows.  Unfortunately, I now had this poor machine loaded down with both Windows *and* Linux at the same time.  NeatLikeDigitalWatches, at least for this underpowered machine.

So, I shut down [coLinux][colinux] and checked out [ext2fsd][ext2fsd] but couldn't get write support working.  After that, [Ext2FS Anywhere][ext2fs3] seems to have done a decent job of bridging the filesystem gap... though now I'm getting all kinds of odd errors and reports of resources running out.  Now, I'm thinking there might be some voodoo conflicts going on here, and early onset of [DLL Hell][dllhell].

But, ignoring the waves of voodoo for now, I was jonesing for a Unix fix, so I installed [Cygwin][cygwin].  I like [Cygwin][cygwin].  But, a little ways into things, trying to get [MySQL][cygwinmysql] working, I'm starting to miss my Debian install and apt-get.  (Gentoo's emerge isn't too bad either, though the compiling-from-source thing gets old.)

Bah.  Thinking I might reformat and try out a Gentoo install now.

Now, I realize that I'm trying to do some very un-Windows things with this WinXP install, and I'm doing it on hardware weaker than the XBox I just recently started hacking around with.  But, just what *do* you do with a machine entirely devoted to Windows, anyway?

And just why can't I get an [ancient game][subspace] working acceptably on my PowerBook under Virtual PC anyway?! 

[cygwinmysql]: http://anfaenger.de/cygwin-1.5/mysql/
[gentoo]: http://www.gentoo.org/
[dllhell]: http://www.ssw.com.au/SSW/Database/DLLHell.aspx
[ext2fsd]: http://ext2.yeah.net
[ext2fs3]: http://www.ext2fs-anywhere.com/
[ut]: http://www.unrealtournament.com/
[subspace]: http://www.subspacehq.com/
[cygwin]: http://www.subspacehq.com/
[colinux]: http://www.colinux.org/
[tv]: http://www.decafbad.com/blog/2004/05/10/homebrew_entertainment_appliances_cheap_open_and_embattled
[account]: http://jeremy.zawodny.com/blog/archives/001962.html
