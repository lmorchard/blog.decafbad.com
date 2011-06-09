--- 
wordpress_id: 439
layout: post
title: Backups with my eyes closed?
date: "2003-07-07T14:45:21-04:00"
wordpress_slug: backup-question
wordpress_url: http://www.decafbad.com/blog/?p=439
---
Okay, so at my new job I'm the Guy if it has a transistor in it.  I'm
developer, sysadmin, and hardware jockey all in one.  This is fun
to a certain extent, since it tests pretty much everything I know from
A through Z.  And so far, I'm doing okay.  Every now and then, though,
I get a bit stumped.
<br /><br />
My most recent adventure involves developing a backup routine for the
office.  I just got tape backup working on a Linux box for a big
Samba-shared directory that we all work out of.  I'm currently winging
it with <code>star</code> and <code>cpio</code> in =CRON=-scheduled scripts that manage a
6-tape rotation for me.
<br /><br />
Full backups on alternating tapes on Fridays,
with incrementals inbetween on tapes labeled by the day.  I even have
the server eject the tape and IM me a few times until I go change to
the day's tape.  Tested recovery, and though it could be smoother, it
is at least possible at the moment.  I figure this is pretty good
for my first personal encounter with managing serious backup.  I plan
to keep researching and to upgrade software at some point soon.
<br /><br />
So, now my boss asks me:  "Hey, can you backup this other folder for me?
I don't want to share it, though, and I don't want you to be able to
read the files."  This folder contains some important yet sensitive
things like salary information and other things to which I have no
business having access.
<br /><br />
My stumper then, is this: How do I grab (or cause to be uploaded) a
folder of files for backup, say as large as 2GB, from a <a href="http://www.decafbad.com/twiki/bin/view/Main/WinXP">WinXP</a> machine,
without having any access myself to read the file contents.  I'll be
able to install whatever I need on the <a href="http://www.decafbad.com/twiki/bin/view/Main/WinXP">WinXP</a> machine, but the idea is
that, when the bits leave that machine for the Linux backup server,
there should be no way for me to read their contents.  But, I must be
able to usefully backup and, in conjunction with the owner of the
files, restore in case of disaster.
<br /><br />
Oh yeah, and I have no budget for software.  So, I'm trying to work
this out using only free tools.
<br /><br />
So, my first though is some sort of encryption on the <a href="http://www.decafbad.com/twiki/bin/view/Main/WinXP">WinXP</a> machine.
Encrypt with GPG or something, leaving my boss with the secret key
on a floppy and the passphrase in his head.  Upload these files
to a special folder on our shared drive, and it all gets backed up
like everything else.
<br /><br />
Or, since I don't even really want to know the names or number of
files in this sensitive folder, can I somehow ZIP up the whole
shebang and encrypt that before uploading?
<br /><br />
Under Linux, none of this would be much of a problem to me.  But,
under <a href="http://www.decafbad.com/twiki/bin/view/Main/WinXP">WinXP</a>, my knowledge of available tools and means of automation
fail me.
<br /><br />
Any hints from out there?
<!--more-->
shortname=backup_question
