--- 
wordpress_id: 698
layout: post
title: SSH and screen, better together
tags: 
- asides
wordpress_slug: ssh-and-screen-better-together
wordpress_date: "2005-09-27T09:21:02-04:00"
wordpress_url: http://decafbad.com/blog/?p=698
---
I've just recently put some pieces together in my head, and have found this to be a very useful invocation to run in a Terminal window on my PowerBook:

`while [ 1 ]; do ssh -t home '/usr/sbin/screen -R work'; done`

*(**Update:** Thanks to a [comment by Leland Johnson](http://decafbad.com/blog/2005/09/27/ssh-and-screen-better-together#comment-2052), I've realized that the above just poorly reinvents [autossh](http://www.harding.motd.ca/autossh/).  Use it instead.)*

Behind the scenes, here's what's up:

* `home` is a host defined in my `~/.ssh/config`;
* `work` is a persistent [`screen`](http://www.gnu.org/software/screen/) session I have running there;
* The `-t` option for `ssh` is key for making `screen` work;
* I have several forwarded ports set up to enable things like IRC and sometimes HTTP proxied through a home machine;
* I have ssh-agent running in order to ensure I never have to enter a password; 
* The `while` loop runs forever, so that whenever my `ssh` connection drops—say when I go from home to work or vice versa—it gets reestablished as soon as possible.

The end result is that I always have a window with a few shells open on a machine at home, as well as a slew of ports tunneled to machines back home to provide a rough sort of VPN.  The connection is usually reestablished and waiting by the time I've gotten settled and get around to visiting that window.
