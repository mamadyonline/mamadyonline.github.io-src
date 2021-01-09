#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mamady Nabé'
SITENAME = 'Mamady Nabé'
SITEURL = 'http://mamadyonline.github.io'
COPYRIGHT_START_YEAR = '2018-2019'
TITLE = 'Mamady Nabé'
DESCRIPTION = "Mamady Nabé est actuellement un doctorant en informatique au sein du laboratoir LPNC."

LOGO_IMAGE = '/theme/static/images/logo.png'

PATH = 'content'
THEME = 'theme'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ABOUT_PAGE_HEADER = 'Bienvenue sur le Blog de Mamady.'

# NOTEBOOK_DIR = 'notebooks'
# EXTRA_HEADER = open('_nb_header.html').read()#.decode('utf-8')

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
# PLUGINS
PLUGIN_PATHS = ['pelican-plugins', 'pelican_dynamic']
PLUGINS = [
    'assets', 
    'pelican_dynamic', 
    'render_math', 
    'pelican_gist'
]

STATIC_PATHS = ['images', 'notebooks']

NAVIGATION = [
    {'site': 'twitter', 'user': 'Mamady Nabé', 'url': 'https://twitter.com/MamadyNabeke'},
    {'site': 'github', 'user': 'madyKing', 'url': 'https://github.com/mamadyonline'},
    {'site': 'linkedin', 'user': 'Mamady', 'url': 'http://linkedin.com/in/mamady'},
    {'site': 'quora', 'user': 'Mamady Nabé', 'url': 'https://fr.quora.com/profile/Mamady-Nab%C3%A9'},

]

TWITTER_NAME = 'MamadyNabeke'
TWITTER_CARDS = True
FACEBOOK_SHARE = True
# QUORA_SHARE = ''
# Social widget
SOCIAL = (('LinkedIn', 'http://linkedin.com/in/mamady'),
          ('GitHub', 'https://github.com/mamadyonline'),
          ('Twitter', 'https://twitter.com/MamadyNabeke'),
          ('Quora', 'https://fr.quora.com/profile/Mamady-Nab%C3%A9'),
          ('Mail', 'mamady.nabe@outlook.com'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#### Analytics
GOOGLE_ANALYTICS = "UA-116900970-1"
DOMAIN = "mamadyonline.github.io"

## Disqus
DISQUS_SITENAME = "mamadyonline"

# Other
LOAD_CONTENT_CACHE = False
