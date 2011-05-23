--- 
wordpress_id: 1735
layout: post
title: I (used to) like rev="canonical"
wordpress_url: http://decafbad.com/blog/?p=1735
---
*Update 4/14*: So, I liked `rev="canonical"`, but I like the notion of pages offering sets of alternative URLs better.  [There are enough cracks in the case](http://www.mnot.net/blog/2009/04/14/rev_canonical_bad) for `rev="canonical"` to stop caring about it and instead focus on the notion behind it.  However it's expressedâ€”is it [`rel="shortlink"`](http://groups.google.com/group/shortlink) now?â€”the final remaining things I'd like to see are:

* An more generalized scope for alternate URL choices asserted by publishers, not just URL shortening.  Other criteria beyond character length include ease of entry on mobile devices (eg. short, but also simple, maybe mostly numeric), ease of verbal mention (eg. billboards, postcards, etc).

* HTTP headers are great where availableâ€”hooray for HEADâ€”but it still needs to be in the page for publishers who can't set custom headers.

* Microformats are great, but I'd rather not parse a whole page to the footer to lift out the desired URLs.

* Don't panic. Have fun.

And with that, I'm going to try coming up with other things to write about so this blog doesn't stay dormant.  The rest of this entry remains unedited below...

<!--more-->
<hr />

<strike>So, like it says up there: I like [rev="canonical"](http://revcanonical.appspot.com/).</strike>

Basically, it's a way of sayingâ€”instead of using that 3rd-party service *you* like for munging *my* URLs, use one of these pre-munged URLs I've provided.  Ideally, the URLs I provide will be shorter for your needs, but my URLs won't be subject to [potentially distasteful things I object to with respect to a service you might pick](http://joshua.schachter.org/2009/04/on-url-shorteners.html).

I like keeping control of URL spaces in the hands of their publishers.  This also opens the field for more individual choice in URL shortening services, allowing more people to try their hand at building a better mouse trapâ€”or allowing publishers to opt out of the mess altogether.  

And, apropos of that, I tend to like `rev="canonical"` as the means of expressing this choice.

There's a lot more background on this whole shebang, but I'll just stick to my $0.02 on the discussion so far.

### [It's too alpha geeky to get adoptedâ€”also: NERDS!](http://www.25hoursaday.com/weblog/2009/04/11/revcanonicalDiggBarOutrageCausesBadIdeasToComeOutOfTheWoodWork.aspx)

Alpha geeks write plugins for web publishing systems used by less-alpha geeks, who eventually install web publishing systems for those even further down the geek scale.  It's not unheard of for something incredibly nerdy to become relatively common, if it proves useful.

Feed auto-discovery is in blogging software and browsers nowâ€”it was once considered a somewhat arcane usage of the `rel` attribute on `<link>` tags in HTML `<head>`.

### [Everyone needs to implement their own URL shortener.](http://www.25hoursaday.com/weblog/2009/04/11/revcanonicalDiggBarOutrageCausesBadIdeasToComeOutOfTheWoodWork.aspx)

No, but everyone gets to pick a shortener for their own URLsâ€”which could coincidentally be self-hosted or third-party.  Isn't the web great?

### [The `rev` attribute is too hard to understand, people will get it wrong](http://benramsey.com/archives/a-revcanonical-rebuttal/).

I hadn't paid much attention to the `rev` attribute until a week or so ago.  I [read the HTML spec on links](http://www.w3.org/TR/html401/struct/links.html#adef-rev) again.  Within 10 minutes of reading the spec, my understanding became this:

* `rel="{X}"` â€” "this link means {X} in relation to the current page".
* `rev="{X}"` â€” "this current page means {X} in relation to this link".

I may have misunderstood itâ€”if so, explain to me how and I'll admit it's harder to understand than I think.  There are harder concepts in the HTML 4 spec.

### The `rev` attribute is removed in HTML5

That's too bad for HTML5.  

[The rationale given for the removal](http://lists.whatwg.org/pipermail/whatwg-whatwg.org/2006-July/006888.html) seems sensible enough.  But, I'd say the rationale for removal is weakened if someone finds a use for the attribute and uses it correctly.

### `rel="shorter"` / `rel="short"` is better and more explicit.

I like this idea in general, and I don't *really* care strongly enough about `rev="canonical"` vs `rel="short"` to make much noise beyond this blog post.  

But, I prefer the semantics of `rev="canonical"`, I don't think `rel="short(er)"` is better, and actually I think the less explicit assertion is a feature.  I've not yet been convinced otherwiseâ€”but realistically, if either catches on, I'll probably use the most popular.

### `rev="canonical"` doesn't mean "shorter URL"

That's okayâ€”what if I don't *want* you to have shortened versions of my URLs?  Doesn't fit in your tweet?  Screw you.  I didn't want you to link to me that badly anyway.  Bah.  

That, of course, is self-defeating.  Conventional use of the attribute will probably yield shorter URLs out of self-interest.  Furthermore, I could even offer a half-dozen URL variations, and you could use the string length function in the language of your choice to pick one on the basis of shortness.  There's a lot of choice to go around here.

Also, feed auto-discovery links don't always lead to truly alternate versions of the current pageâ€”but instead to a useful set of items, many of which may currently appear somewhere on the page.  So, even the "clear" semantics have some play in them as used in the wild.

### [A `rev="canonical"` HTTP header is better.](http://shiflett.org/blog/2009/apr/a-rev-canonical-http-header)

Hmm, maybe.  It would certainly allow for possibly lighter-weight HEAD requests in determining the alternative URL for a given URL.  But, I would expect it to fall apart in collections of static HTML pages baked by an offline script where web server configuration might not make setting custom headers easy.

Not everyone has the luxury / inclination to have a dynamic language capable of setting headers running in their web server.

### [`rev="canonical"` should appear on hyperlinks in the body of the page](http://adactio.com/journal/1568/)

[I like microformats](http://decafbad.com/blog/2005/05/08/whats-old-scraping-is-new-again-microformats), [in general](http://decafbad.com/blog/2005/05/17/magic-microformat-forms).  But, I don't really want to potentially parse a whole page to find the shorter URL that might be in the footer.  With `rev="canonical"` in the `<head>`, I only have to parse so far before I find it or give up.

There's a lot of prior art on this with relation to feed autodiscoveryâ€”we used to mainly look for RSS feed URLs inside the page, too.  It sucked.

### [Claiming to be canonical for another URL is trouble.](http://benramsey.com/archives/a-revcanonical-rebuttal/#comment-288465)

Okay, how about requiring a reciprocal `rel="canonical"` on the same page with `rev="canonical"`.

Trust but verifyâ€”and only accept `rev="canonical"` where `rel="canonical"` matches the current URL *and* `rev="canonical"` yields a 301 redirect to the `rel="canonical"`.

I can't see this verification process being necessarily more burdensome than using a 3rd-party shortener APIâ€”and that's *if* you're paranoid and building an index that needs some measure of resistance to gaming.

### [A single character slip from `rev="canonical"` to `rel="canonical"` could wreck your Googlejuice!](http://samj.net/2009/04/revcanonical-considered-harmful.html?showComment=1239617160000#c7231589643969293690)

So, don't do that.  

Maybe Googlejuice should be more resilient.  Maybe it actually isâ€”has anyone actually soured their juice yet with a mistake like this and lived to tell the tale?  

Either way, characters mean things in computer languages, so make sure you use the right ones in the right order.

### You guys are moving on this stuff too fast!

Welcome to 2002, when lots of us had more spare time than employment and we deployed new crap like this on our blogs and sites daily.  

Back in those olden days, we manipulated raw HTML with our bare hands and deployed radioactive code using our teethâ€”all without benefit of protective change control.  We probably all have cancer of the access logs now, but it was all in the name of Web Science!

### Too long; didn't read

So, yeah.  I like the idea behind `rev="canonical"` and I prefer its expression as `rev="canonical"` bestâ€”but the idea is the important thing.  Let's get over the expression part fast and spend more time exploring the nuts and bolts and implications of the concept itself.
