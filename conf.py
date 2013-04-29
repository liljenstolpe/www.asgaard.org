# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://posativ.org//conf.py.html

TITLE = ('Missing the', 'forest')

SITENAME = 'Musings on random topics'
WWW_ROOT = 'http://www.asgaard.org/'

AUTHOR = 'Christopher Liljenstolpe'
EMAIL = 'blog@cdl.asgaard.org'

DEPLOY_DIR = 's3://www.asgaard.org/'

FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']
VIEWS = {
    '/': {'filters': 'summarize', 'view': 'index',
          'pagination': '/page/:num/'},

    '/:year/:slug/': {'view': 'entry'},

    '/tag/:name/': {'filters': 'summarize', 'view':'tag',
                    'pagination': '/tag/:name/:num/'},

    '/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    '/:slug/': {'view': 'page'},  # static pages
    '/articles/': {'view': 'articles'},
    '/sitemap.xml': {'view': 'sitemap'},

}

THEME = 'shadowplay'
ENGINE = 'acrylamid.templates.jinja2.Environment'

DISQUS_SHORTNAME = 'asgaard'

DEFAULT_ORPHANS = 3

# Tuples are (name, link)
BLOGROLL = [
    ('Some of my photographs', 'http://gallery.liljenstolpe.org/'),
    ('My Github repo', 'http://www.github.com/liljenstolpe')
]

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_START_INDEX = 0
TAG_CLOUD_SHUFFLE = True

DEPLOYMENT = {
    "ls": "ls $OUTPUT_DIR",
    "echo": "echo '$OUTPUT_DIR'",
    "default": "s3cmd sync $OUTPUT_DIR/ $DEPLOY_DIR"
}
