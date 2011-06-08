---
layout: post
title: Moved to Jekyll and Disqus
---
**TL;DR**: <em>My blog is now produced by [Jekyll][], with comments hosted by [Disqus][].</em>

[jekyll]: https://github.com/mojombo/jekyll
[disqus]: http://disqus.com/

This blog has transitioned between a handful of publishing platforms -
including Movable Type, blosxom, and Wordpress. Well, apparently, it's that
time again.  I've been toying with making a change again for a few years,
and finally just got all the pieces together over the past week. This blog
is now just a pile of static files produced by [Jekyll][], and the comments
are now hosted by [Disqus][].

[pages]: http://pages.github.com/

This has a lot of interesting implications:

* I can neglect my server for long periods of time without worrying that my
  long-outdated copy of Wordpress has been exploited. Really, there's no
  reason for me to have a full-featured CMS running here.

* I could host my entire blog on Amazon S3 or something similar, and be
  more neglectful by reducing active code even further. The only crappy
  thing is that I don't think I can send `decafbad.com` directly to S3, and
  would need to redirect to a CNAME on a subdomain on `blog.decafbad.com`.

* I can edit my blog directly on GitHub and, assuming I get the webhooks
  set up, have my server rebuild the HTML automatically on a `git push`. I
  could probably use [GitHub Pages][pages] and the Jekyll support there,
  but I suspect I'll be doing some Weird Things that they won't handle.
  (And probably for good reason.) 

* Since Disqus has all my comments now, I can stop worrying about running
  that code on my server too. I'm a little antsy about putting that in the
  cloud, but the escape routes are well lit and I should be able to replace
  it easily if I need to. Self-hosted, JS-include-based comments is a
  project in my TODO list.

* My writing here is now all stored in individual text files, formatted with
  Markdown, annotated with YAML metadata, and subject to revision control
  under git. This combination feels like it has a lot of longevity and
  potential for survival even beyond this current experiment with [Jekyll][]

* Writing, editing, and publishing entries here can now more closely match
  my daily reality of living in MacVim and git. It sounds lame, but the
  notion of swapping over to a Wordpress admin page and working in a
  browser textarea has often kept me from even starting a post.

But, some things are broken, now:

* No more tag pages. I don't think very many humans visit these pages, but
  a lot of search engines do.

* No more tag feeds. I expect to hear about this soon, since this blog gets
  syndicated to Planet Mozilla via my "mozilla" tag feed.

* No more year / month archive pages or sidebar widget. Not sure how many
  people actually stroll down memory lane here on my blog, but I do have a
  [gigantor huge list of all my posts evar][archives], now.

* A general lack of contextual links to related posts and such. Turns out
  that running the LSI option on Jekyll is completely horrible.

The bright side is that there are solutions to all the broken things, and
now I have something to tinker with again on my blog.  So, let me know if
anything else looks broken, and hopefully this will get me spewing some
more words out onto this thing soon.

[archives]: http://decafbad.com/blog/archives
