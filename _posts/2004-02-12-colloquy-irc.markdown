--- 
wordpress_id: 513
layout: post
title: Colloquy, an insane IRC client for OS X
wordpress_slug: colloquy-irc
wordpress_date: "2004-02-12T21:50:53-05:00"
wordpress_url: http://www.decafbad.com/blog/?p=513
---
<blockquote cite="http://fishbowl.pastiche.org/2004/02/05/a_confluence_gui_client_in_200_lines_of_code">WebKit is so insanely easy to use that I'm amazed every OS X application doesn't do it somewhere, just for the fun of it. Maybe they do.</blockquote>
<div class="credit" align="right"><small>Source:<cite><a href="http://fishbowl.pastiche.org/2004/02/05/a_confluence_gui_client_in_200_lines_of_code">The Fishbowl: A Confluence GUI Client in 200 Lines of Code</a></cite></small></div>

<blockquote cite="http://www.javelin.cc/colloquy/developers.html">A new major feature of Colloquy 2 are the extensible conversation styles. Styles are simple OS X bundles wraped around a CSS file (at minimum) or a CSS file and a XSL file. Knowing this, the fact that Colloquy uses XML to store chat messages that come in over the network is no surprise to some. Pairing these three technologies gives us great flexibility when processing and displaying a message on screen.
<br /><br />
The process of formatting a message follows these steps, start to finish. First, wrap the message in a simple XML envelope, encoding any special characters and representing IRC styling as XHTML. This XML envelope gets transformed with the curent style's XSL file (or a built-in default XSL file). The resulting transformation from the XSL on the XML should be XHTML that can then be rendered with help from the style's CSS file. Rendering is done via Apple's Safari (WebKit) engine -- so the possibilities are endless (evidenced by the built-in iChat like Bubbles style).</blockquote>
<div class="credit" align="right"><small>Source:<cite><a href="http://www.javelin.cc/colloquy/developers.html">Colloquy: Developers</a></cite></small></div>

<p>
Colloquy is an IRC client for OS X that I just discovered this week,
via <a href="http://macslash.org/article.pl?sid=04/02/09/1649200&mode=thread">an article posted on MacSlash</a>.
I've been looking for a decent Cocoa-based app as an alternative
to my use of <a href="http://xchataqua.sourceforge.net/">X-Chat Aqua</a>,
<a href="http://www.conversation.pwp.blueyonder.co.uk/">Conversation</a>, and
<a href="http://www.irssi.org">irssi</a>.  Having never heard of Colloquy before,
I figured I'd check it out.
</p>

<p>
Colloquy is a Cocoa app, and the source is available.  It's the first OS X
IRC client I've played with yet that most resembles what I expect out of a modern
Cocoa app.  Conversation is right there, too, but I don't see any source (no
offence to the author) and it doesn't yet support multiple servers or AppleScript
(although those are on the planned features list).
</p>

<p>
Beyond all that, though, what has sucked me into Colloquy is the way IRC messages are
presented and styled.  In case the introductory quotes haven't given you the idea, this
thing pipelines XML, XSL, CSS, HTML, Javascript, and WebKit to provide
an immensely flexible user-customizable, modular display style system.
There aren't that many styles yet, but conceivably anything one could
do with the pile of technologies above can be employed in presenting IRC
messages.
</p>

<p>
Yes, you could make the case that this is an insane example of overkill.
If so, Conversation or a shell-based program is likely more your speed.
Admittedly, Colloquy is not a featherweight IRC client.
But I've been thinking about this sort of inversion of web tech for awhile.
Instead of the browser hosting the app, the app hosts the browser.  I've been
doing a ton of tinkery UI work with HTML and JavaScript in my
<a href="http://www.decafbad.com/cvs/dbagg2/">news aggregator</a> and have come
to appreciate the DOM and various things JavaScript makes possible in modern
browsers.
</p>

<p>
This has lately lead me to consider how a browser canvas
could be used as a sort of universal widget inside a native app... not at
all unlike the way Colloquy uses it.  Apple's WebKit encapsulation makes it
just about <a href="http://cocoadevcentral.com/articles/000077.php">dead simple</a>
to drop it into an app and integrate it.  In fact,
from a shallow glance at the docs for WebKit, it seems even simpler to use than
some other GUI widgets in the Cocoa arsenal.
</p>

<p>
So...  is this the start of more Cocoa apps embedding WebKit views, "just for the
fun of it"?  Who knows, but it really appeals to my propensity for mixing and
matching different tech within the same project.  I suppose it's a sort of sick
addiction I've picked up from the Tower of Babel web development I've been doing
for years, but it looks like fun to me!
</p>
<!--more-->
shortname=colloquy_irc
