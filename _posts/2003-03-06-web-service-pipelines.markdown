--- 
wordpress_id: 390
layout: post
title: Building Pipelines with Web Services
wordpress_url: http://www.decafbad.com/blog/?p=390
---
So <a href="http://www.decafbad.com/blog/tech/old/oooodh.html" target="_top">on this day last year</a>,
I was excitely thinking about pipelining webservices together like commands in a
UNIX command line shell.  Lately, I've been doing quite a bit of work at the
command line level, more so than I ever have before.  And for all the clunkiness
and inelegances to be found there, I think the zen has stuck me.
<br /><br />
Sure, it's an ass-ugly string of characters that connects commands
like find, sort, awk, sed, grep, and ssh together.  But, in constructing such
monstrosities, I find myself generating new disposable tools at a rate
of at least one every minute or so.  And, though a few have found themselves graduating
into fuller, cleaner, more general tools, I would have been stuck for
hours were it not for a quick multi-file grep across a vast plain of comma-separated
value files digested by a tag team of sed and awk.  Then, like magic, I toss in
an incredibly slow yet, at the time, convenient call to mysql on another server
behind a firewall via ssh with a SQL call constructed from the regurgitations
of said sed and awk brothers.
<br /><br />
So, I'm thinking again:  How hot would this be if it were web services replacing
each of my commands?  How hot would it be if there was a STDIN, STDOUT, and STDERR
for a whole class of web services?  Imagine an enhanced bash or zsh piping these
beasts together.  For awhile, I thought my <a href="http://www.decafbad.com/twiki/bin/view/Main/XmlRpcFilteringPipe">XmlRpcFilteringPipe</a> API was the way to
go, but lately I've been thinking more in the direction of <a href="http://www.decafbad.com/twiki/bin/view/Main/REST">REST</a>.  I have to admit
that the XML-RPC API is a bit clunky to use, and besides, no one's really paid
it much notice besides using it in the peculiar fashion I do to make my <a href="http://www.decafbad.com/twiki/bin/view/Main/WeblogWithWiki">WeblogWithWiki</a>.
<br /><br />
How about this for a simpler API:  Post data to a URL, receive data in response.
There's your STDIN and STDOUT.  What about STDERR?  Well, I suppose it's an
either-or affair, but standard HTTP header error codes can fill in there.  What
about command line arguments?  Use query parameters on the URL to which you're
posting.  This all seems very web-natural.
<br /><br />
Now I just have to write a shell that treats URLs as executable commands.
<!--more-->
shortname=web_service_pipelines
