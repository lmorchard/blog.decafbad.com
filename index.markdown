---
layout: default
---
<article id="index">
## Recent Blog Posts

<ul class="posts">
    {% for post in site.posts limit:15 %}
        {% include item.html %}
    {% endfor %}
</ul>

[Full archive](archives)
</article>
