--- 
wordpress_id: 484
layout: post
title: Dynamic polling times for news aggregators, II
wordpress_slug: dynamic-polling-freq-too
wordpress_date: "2003-09-29T13:48:28-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=484
---
<p>
Okay, so that <a href="http://www.decafbad.com/blog/tech/dynamic_feed_scan_times.html">thing with the SQL</a> I did Friday?
I'm not exactly sure what I was thinking with it.  I was doing something
that seems really odd now, trying to collect counts of new items together
by hour, then averaging those hourly counts across a week.  Instead, I'm
trying this now:
</p>

<pre>SELECT
  source,
  'update_period' AS name,
  round(min(24,max(1,(max(1,(iso8601_to_epoch(max(created)) -
    max(now() - (7*24*60*60), iso8601_to_epoch(min(created)))) /
   (60*60))) / count(id))),2) AS value
FROM
  items
WHERE
  created >= epoch_to_iso8601(now() - (7*24*60*60)) 
GROUP BY
  source</pre>

<p>
This bit of SQL, though still ugly, is much simpler.  This leaves out
the subselect, which I think I might have been playing with in order
to build a little graph display of new items over time by source.  What
the above does now is to get an average time between new items for the
past week, with a minimum of an hour, and a maximum of a day.  This
seems to be working much better.
</p>

<p>
An alternate algorithm I've been playing with was suggested in
<a href="http://www.decafbad.com/comments/tech/dynamic_feed_scan_times/#comment-aofdehdefioofcb">a comment</a>
by <a href="http://24.102.209.201/weblogs/ben/">Gnomon</a>,
inspired by TCP/IP's Additive Increase / Multiplicative Decrease.
With this, I subtract an hour from the time between polls when a
poll finds new items, and then multiply by 2 every time a poll
comes up with nothing new.
</p>

<p>
Using the average of new items over time lessens my pummeling
of servers per hour, but the second approach is even lighter
on polling since it's biased toward large leaps backing off
from polling when new items are not found.  I'll likely be trading
off between the two to see which one seems to work best.
</p>

<p>
Hoping that, after playing a bit, I'll settle on one and my
aggregator will play much nicer with feeds, especially once
I get the HTTP client usage to correctly use things like
last-modified headers and ETags.  There's absolutely no reason
for a news aggregator to poll a feed every single hour of a day,
unless you're monitoring a feed that's mostly quiet, except
for emergencies.  In that case, well, a different polling
algorithm is needed, or maybe an instant messaging or pub/sub
architecture is required.
</p>

<p>
<b>Update:</b> As <a href="http://24.102.209.201/weblogs/ben/">Gnomon</a>
has corrected me in comments, I've got the AIMD algorithm mixed up.
What I really should be doing is making quick jumps up in polling
frequency in response to new items (multiplicative decrease of
polling period) and creeping away in response to no new items
(additive increase of polling period).  As he notes, this approach
should make an aggregator jump to attention when clumps of new
posts come in, and gradually get bored over periods of silence.
I've adjusted my code and will be tinkering with it.
</p>

<p>
Also, although <a href="http://24.102.209.201/weblogs/ben/">Gnomon</a> makes
a good point that bloggers and their posting habits are not easily
subject to statistical analysis,
I've further refined my little SQL query to catch sources
which haven't seen any updates during the week (or ever):
</p>

<pre>SELECT 
  id as source,
  'update_period' AS name,
  round(min(24,max(1,coalesce(update_period,24)))) AS value
FROM sources
LEFT JOIN (
     SELECT
      source AS source_id,
            (iso8601_to_epoch(max(created)) -
              max(
                now()-(7*24*60*60),
                iso8601_to_epoch(min(created))
              )
            ) / (60*60) / count(id)
        AS update_period
    FROM items
    WHERE created >= epoch_to_iso8601(now() - (7*24*60*60)) 
    GROUP BY source
) ON sources.id=source_id</pre>

<p>
Also, in case anyone's interested, I've checked <a href="http://www.decafbad.com/cvs/dbagg/lib/dbagg/scan.py?rev=HEAD&content-type=text/vnd.viewcvs-markup">all the above</a>
into CVS.  This beastie's far from ready for prime time, but it
might be interesting to someone.
</p>
<!--more-->
shortname=dynamic_polling_freq_too
