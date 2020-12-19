#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Zarco Dionisio'
SITENAME = 'Mictlan Forensic'
SITEURL = ''
SITESUBTITLE = "Ciencias Forenses"


PATH = 'content'
STATIC_PATHS = ['img']

TIMEZONE = 'Mexico/General'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/MictlanForensic'),
         ('Instagram', 'https://www.instagram.com/mictlanforensic'),
         ('Twitter', 'https://twitter.com/MictlanForensic'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/arkreuz/Workspace/MicFor/Themes/Flex-master"
DISPLAY_PAGES_ON_MENU = None
BOOTSTRAP_THEME = "amelia"

# Path to Plugins
PLUGIN_PATHS = ['/home/arkreuz/Workspace/MicFor/pelican-plugins']
# Enable i18n plugin, probably you already have some others here.
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


# Default theme language.
I18N_TEMPLATES_LANG = "en"

# Your language.
DEFAULT_LANG = "es_ES"

# Match languages for other configs.
OG_LOCALE = "es_ES"
LOCALE = ("es_ES", "es_ES.utf8")
