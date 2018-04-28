#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'T. Chaitanya Sagar'
SITENAME = 'Hub for Materials Engineering'
SITEURL ='https://sagarchaitanya.github.io/statichome '
#SITEURL = 'http://home.iith.ac.in/~chaitanyasagar'
SITEURL_ABS = SITEURL
SITESUBTITLE = 'ICME and Multiscale Modeling'
EMAIL = 'me14resch11007@iith.ac.in'
PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('IITH', 'http://iith.ac.in'),
        )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/chaitanyasagar.tinku'),('Linkedin', \
'www.linkedin.com/in/chaitanya-sagar-8143a49'), \
('Youtube','https://www.youtube.com/channel/UC-nXT3K2vSejdNdnWkbMIxA?disable_polymer=true'), \
('Github','https://github.com/sagarchaitanya'), ('Email','mailto:me14resch11007@iith.ac.in'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#pelicanconf.py

PLUGIN_PATHS = ['pelican-plugins']
# THEME = "pelican-themes/bluegrasshopper"
# THEME = "pelican-themes/Just-Read"

# THEME = "pelican-themes/bootstrap2"
# THEME = "pelican-themes/dev-random2"
#THEME = "pelican-themes/"


#THEME = "pelican-themes/Just-Read"
#THEME = "pelican-themes/basic"
#THEME = "pelican-themes/bluegrasshopper"
#THEME = "pelican-themes/bold"
#THEME = "pelican-themes/bootlex"
#THEME = "pelican-themes/bootstrap"
#THEME = "pelican-themes/bootstrap2"
#THEME = "pelican-themes/brownstone"
#THEME = "pelican-themes/built-texts"
#THEME = "pelican-themes/cebong"
#THEME = "pelican-themes/chunk"
#THEME = "pelican-themes/crowsfoot"
#THEME = "pelican-themes/dev-random"
#THEME = "pelican-themes/dev-random2"
#THEME = "pelican-themes/elegant"
#THEME = "pelican-themes/fresh"
#THEME = "pelican-themes/gum"
#THEME = "pelican-themes/html5-dopetrope"
#THEME = "pelican-themes/irfan"
#THEME = "pelican-themes/iris"
#THEME = "pelican-themes/jesuislibre"
#THEME = "pelican-themes/lannisport"
#THEME = "pelican-themes/lightweight"
#THEME = "pelican-themes/martyalchin"
#THEME = "pelican-themes/mnmlist"
#THEME = "pelican-themes/monospace"
#THEME = "pelican-themes/neat"
#THEME = "pelican-themes/niu-x2"
#THEME = "pelican-themes/nmnlist"
#THEME = "pelican-themes/notmyidea-cms"
#THEME = "pelican-themes/notmyidea-cms-fr"
#THEME = "pelican-themes/pelican-bootstrap3"
#THEME = "pelican-themes/pelican-cait"
#THEME = "pelican-themes/pelican-mockingbird"
#THEME = "pelican-themes/pelipress"
#THEME = "pelican-themes/plumage"
#THEME = "pelican-themes/pure"
#THEME = "pelican-themes/relapse"
#THEME = "pelican-themes/sneakyidea"
#THEME = "pelican-themes/storm"
#THEME = "pelican-themes/subtle"
#THEME = "pelican-themes/sundown"
#THEME = "pelican-themes/svbhack"
#THEME = "pelican-themes/svbtle"
#THEME = "pelican-themes/syte"
#THEME = "pelican-themes/tuxlite_tbs"
#THEME = "pelican-themes/tuxlite_zf"
#THEME = "pelican-themes/water-iris"
#THEME = "pelican-themes/waterspill"
#THEME = "pelican-themes/waterspill-en"
#THEME = "pelican-themes/"


#THEME = "pelican-themes/sneakyidea"
#THEME = "pelican-themes/pelipress"
#THEME = "pelican-themes/plumage"
#THEME = "pelican-themes/mnmlist"
#THEME = "pelican-themes/martyalchin"
#THEME = "pelican-themes/iris"
#THEME = "pelican-themes/niu-x2"
#THEME = "pelican-themes/monospace"

#THEME = "pelican-themes/chunk"
#THEME = "pelican-themes/crowsfoot"
#THEME = "pelican-themes/dev-random"
#THEME = "pelican-themes/dev-random2"
#THEME = "pelican-themes/elegant"


#THEME = "pelican-themes/html5-dopetrope"
#THEME = "pelican-themes/lannisport"
#THEME = "pelican-themes/nmnlist"


#THEME = "pelican-themes/fresh"
#THEME = "pelican-themes/pelican-cait"
#THEME = "pelican-themes/pelican-mockingbird"
#THEME = "pelican-themes/pure"
#THEME = "pelican-themes/subtle"
#THEME = "pelican-themes/waterspill-en"
#THEME = "pelican-themes/pelican-bootstrap3"
THEME = "pelican-themes/gum"
#THEME = 'pelican-themes/html5-dopetrope'
#BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATHS = ['./pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
    'tipue_search',
    'pelican_youtube' ]

I18N_TEMPLATES_LANG = 'en'

# for Tique Search Plugin
#DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives','right-sidebar','base','disqus_script','left-sidebar')

# extra addition
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

#STATIC_PATHS = [ 'extra' STATIC_PATHS = ['images','attachments']]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

#Modify pelicanconf.py to include the two new pages.


# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top menus
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


