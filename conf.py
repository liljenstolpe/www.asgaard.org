# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://posativ.org//conf.py.html

import subprocess

TITLE = ('Missing the', 'forest')

SITENAME = '(ir)Relevant musings on random topics'
WWW_ROOT = 'http://www.asgaard.org/'

AUTHOR = 'Christopher Liljenstolpe'
EMAIL = 'blog@cdl.asgaard.org'

DEPLOY_DIR = 's3://www.asgaard.org/'

STATIC = [ 'assets' ]

LANG = 'en'
DATE_FORMAT = '%Y-%m-%d, %H.%M'
strptime = '%Y-%m-%d, %H.%M'

# Added to be able to include the git commit code in the base.html file in shadowplay

GIT_COMMIT_SHORT = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
GIT_COMMIT = subprocess.check_output(['git', 'rev-parse', 'HEAD'])

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
    ('Some of my photographs', 'http://gallery.liljenstolpe.org/')
]

SOCIAL = [
    ('Linkedin', 'http://www.linkedin.com/in/liljenstolpe', '/img/linkedin.png'),
    ('GitHub', 'http://github.com/liljenstolpe', '/img/github.png'),
    ('Google+', 'http://plus.google.com/100771440792221683456', '/img/google-plus.png'),
    ('Twitter', 'http://twitter.com/liljenstolpe', '/img/twitter.png'),
    ('Facebook', 'http://www.facebook.com/liljenstolpe', '/img/facebook.png')
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
