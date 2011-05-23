--- 
wordpress_id: 448
layout: post
title: HTTP/1.1 From header and FOAF use in RSS aggregators
wordpress_url: http://www.decafbad.com/blog/?p=448
---
<blockquote cite="http://diveintomark.org/archives/2003/07/21/atom_aggregator_behavior_http_level.html#c003152"><i>Privacy issues aside (for the moment), there is a request header called "FROM", RFC 2616 s14.22 describes it. 

<br /><br />
Now, it does say it should, if given, contain an Internet e-mail address for the human user who controls the requesting user agent.  SHOULD isn't MUST though, so what putting the user's homepage there?

<br /><br />
It also says "In particular, robot agents SHOULD include this header so that the person responsible for running the robot can be contacted if problems occur on the receiving end."</i></blockquote><div class="credit" align="right"><small>Source: <cite><a href="http://diveintomark.org/archives/2003/07/21/atom_aggregator_behavior_http_level.html#c003152">eric scheid: Atom aggregator behavior (HTTP level) [dive into mark]</a></cite></small></div>	<p>Ask a <a href="http://diveintomark.org/archives/2003/07/21/atom_aggregator_behavior_http_level.html#c003136">stupid question</a> , get a <a href="http://diveintomark.org/archives/2003/07/21/atom_aggregator_behavior_http_level.html#c003152">smart answer</a> .</p>

	<p>Last year, I thought it was a good idea to <a href="http://www.decafbad.com/blog/tech/old/oooahe.html">abuse referers</a> in order to leave footprints behind when I consume <span class="caps">RSS</span> feeds.  Then, this past January, the abuse in the practice was revealed and <a href="http://www.decafbad.com/blog/tech/old/ooodoe.html">using the User-Agent header</a> was recommended for this.</p>

	<p>So, just for the hell of it, I <a href="http://diveintomark.org/archives/2003/07/21/atom_aggregator_behavior_http_level.html#c003136">asked about the User-Agent header</a> for use in the context over at <a href="http://www.diveintomark.org">Mark&#8217;s place</a> to see what responses I&#8217;d get.  The one that seemed most informative was from <a href="http://IAwiki.net/EricScheid">Eric Scheid</a> as quoted above, referring me to <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.22">the <span class="caps">HTTP</span>/1.1 spec, section 14.22</a></p>

	<p>As per Eric&#8217;s comment and the spec, the value of a &#8220;From&#8221; header <span class="caps">SHOULD</span> be an email address, but I would think that using a <span class="caps">URL</span> wouldn&#8217;t be <strong>too</strong> much an abuse of this header.  Seems like a good idea to stick either the <span class="caps">URL</span> to a blog here, or even better, stick the <span class="caps">URL</span> to your <span class="caps">FOAF</span> file here.</p>

	<p>I&#8217;d really like to see this get built into aggregators as an option, though not turned on by defauilt for privacy&#8217;s sake.  I like the idea of leaving my name or a trail back to me at the doorstep of people whose feeds I&#8217;m reading, and I like the idea of standardizing the practice as cleanly as possible.  Using the &#8220;From&#8221; header seems to be the best option so far, versus header abuse and User-Agent overloading.</p>

	<p>Man.  One of these days, I really have to get around to studying those specs in full, rather than just sporadically referencing them.  Thank goodness for smart guys like <a href="http://www.diveintomark.org">Mark</a> and <a href="http://IAwiki.net/EricScheid">Eric</a> (among others) who actually take the time to read these things and try to communicate the gist to the rest of us busy developers!</p>
<!--more-->
shortname=from_foaf_rss
