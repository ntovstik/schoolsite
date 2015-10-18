#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Natalia Tovstik'
SITENAME = u'Українська школа в Амстердамі'
#SITEURL = 'http://ua-school-amsterdam.org'
SITEURL = 'http://127.0.0.1:8000'

#PATH = 'content'
THEME = 'themes/backdrop'
#THEME='pelican-chameleon'
#THEME='themes/waterspill-en'
#THEME='/home/nmi/natasha/pelican-themes/BT3-Flat'
#THEME='/home/nmi/natasha/pelican-themes/blue-penguin'
#THEME='/home/nmi/natasha/pelican-themes/simple-bootstrap/'
#THEME='themes/twenty-pelican-html5up'

SITE_DESCRIPTION='Вітаємо Вас на сайті української школи в Амстердамі.<br/> Наши контакти: e-mail: oksana.guseletova@gmail.com, тел. +31612727194'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Українське посольство в Нідерландах', 'http://mfa.gov.ua/ua/'),)


# Social widget
SOCIAL = (('Facebook', 'https://m.facebook.com/profile.php?id=586437808129476&ref=bookmarks'),
          )

DEFAULT_PAGINATION = 10
#PAGE_ORDER_BY = 'sortorder'

STATIC_PATHS = ['images', 'fonts', 'css', 'js']
ARTICLE_PATHS = ['articles']

PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AUTHORS = {   
    u'nata': 'http://nata.info'    
}

BACKDROP_IMAGE = 'http://127.0.0.1:8000/images/Amsterdam1.jpg'
#PROFILE_IMAGE = 'images/apartment-13.jpg'
#PROFILE_IMAGE = 'images/Amsterdam1.jpg'

