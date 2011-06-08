---
layout: default
---

## About Me

Hi there! My name is Leslie Michael Orchard. I'm a [serially enthusiastic][serial],
caffeine-dependent {web,mad,computer} scientist and [{tech,scifi}][author] writer 
working for the [Mozilla Corporation][webdev] and living near [Ann Arbor][annarbor] /
[Detroit][detroit] in Michigan.

[serial]: http://decafbad.com/blog/2006/05/26/confessions-of-a-serial-enthusiast
[author]: http://www.amazon.com/Leslie-M.-Orchard/e/B001JS692K/ref=sr_tc_2_0?qid=1268277758&sr=1-2-ent
[webdev]: https://wiki.mozilla.org/Webdev
[annarbor]: http://arborwiki.org/index.php/Main_Page
[detroit]: http://www.detroitmakeithere.com/

## Recent Blog Posts

<ul class="posts">
    {% for post in site.posts limit:10 %}
        {% include item.html %}
    {% endfor %}
</ul>

[Full archive](archive)
