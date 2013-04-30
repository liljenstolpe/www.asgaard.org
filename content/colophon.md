---
title: colophon
type: page
---

I've decided to start blogging again, and looking around at the
landscape, decided to do a static blog, which is file and text
driven.  Less things to go wrong, less things to fix.  We'll see how
it goes.
Below, I've outlined some of the technologies and packages that I am
currently using.  I will try to keep this up-to-date as it evolves.

## Blogging package ##
I'm using [Acrylamid](http://posativ.org/acrylamid/) version
[0.72](https://github.com/posativ/acrylamid/).  I started off using
[Octopress](http://octopress.org/), and while it was quite flexible
and had more features than I needed, I am a Python guy (if anything)
and the Ruby setup was a bit more problematic than I wanted to deal
with for a simple blog.

## Theme ##
The theme in use is an [HTML5](http://dev.w3.org/html5/spec/) theme
called *Shadow Play 2* from the great folks at
[HTML5webtemplates](http://www.html5webtemplates.co.uk/).  I've
modified it a bit to change the footer, changed the style of the
sidebar links, and changed the logo image.  Those changes can be found
in my [github
repository](https://github.com/liljenstolpe/www.asgaard.org/) for this
site.

### Logo image ###
The picture of the trees used in the header can be found at
[wallpaperscraft.com](http://wallpaperscraft.com/wallpaper/wood_black-and-white_from_below_trees_gloomy_kroner_fog_silence_60216).

## Version Control ##
I'm using a public [github
repository](https://github.com/liljenstolpe/www.asgaard.org/) to
version control this blog.  I display the commit hash used to generate
the version being served in the footer of the page.

## Web Server ##
A public [Amazon S3](http://aws.amazon.com/s3/) bucket serves all the
content out.  I followed the recipe that Amazon provides
[here](http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html).
However, I do not use [Route53](http://aws.amazon.com/route53/), but
instead use my own DNS servers.


