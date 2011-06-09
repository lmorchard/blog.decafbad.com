--- 
wordpress_id: 552
layout: post
title: Markdown formatting for Kwiki
excerpt: I just made my first Kwiki formatting plugin, making Markdown formatting available.
date: "2004-09-18T19:20:41-04:00"
tags: 
- wiki
wordpress_slug: markdown-formatting-for-kwiki
wordpress_url: http://www.decafbad.com/blog/?p=552
---
I just made my first Kwiki formatting plugin, making [Markdown][markdown] formatting available.  I'm not sure that it's completely working, but maybe if I get over the lazy threshold, I'll package it up and ship it up to CPAN.  For what it's worth, here it is:

    package Kwiki::Markdown;
    use strict;
    use warnings;
    use Kwiki::Plugin '-Base';
    use mixin 'Kwiki::Installer';
    
    use Markdown;
    
    const class_title => 'Markdown';
    const class_id => 'markdown';
    
    sub register {
	my $registry = shift;
	$registry->add( wafl => markdown => 'Kwiki::Markdown::Wafl' );
    }
    
    package Kwiki::Markdown::Wafl;
    use base qw( Spoon::Formatter::WaflBlock );
    
    sub to_html {
       Markdown::Markdown($self->block_text);
    }
    
    package Kwiki::Markdown;
    __DATA__
    
And, not that I planned it this way, but I just realized that I'm wearing my [Daring Fireball t-shirt][tshirt] this very moment.  Heh, heh.

[markdown]: http://daringfireball.net/projects/markdown/
[tshirt]: http://daringfireball.net/members/
