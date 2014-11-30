#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# site settings
AUTHOR = 'Lennyh'
AUTHORS = ['Lennyh']
SITENAME = '佛说'
SITEURL = 'http://localhost:8000'
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
DEFAULT_PAGINATION = 8

USE_FOLDER_AS_CATEGORY = True # folder as category
DEFAULT_CATEGORY = '未分类'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 50
WITH_FUTURE_DATES = False # set to false so future date for draft

OUTPUT_RETENTION = (".git", ".hg", ".bzr", ".svn")
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
STATIC_PATHS = ['images']
DEFAULT_METADATA = (
        ('authors', 'Lennyh'),
        ('lang', 'zh'),
        )

#TEMPLATE_PAGES = {'src/books.html': 'dest/books.html'}
# for index page
#DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')

# code highlight options
PYGMENTS_RST_OPTIONS = {
        'linenos':'inline',
        }

# for printer
TYPOGRIFY = False

# timezone and locales
DEFAULT_LANG = 'zh'
DEFAULT_DATE = 'fs'     # default use filesystem timestamp
TIMEZONE = 'Asia/Shanghai'
LOCALE = ('zh_CN.UTF-8', 'en_US.UTF-8')
DATE_FORMATS = {
        'zh_CN':'%Y-%m-%d(%a)',
        'en_US':'%a, %d %b %Y',
        }
DEFAULT_DATE_FORMAT = DATE_FORMATS.get('zh_CN')

JINJA_EXTENSIONS = []

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
'cjk-auto-spacing',
#'better_figures_and_images',
#'code_include',
'collate_content',
#'filetime_from_git',
'neighbors',
#'pdf',
'pin_to_top',
#'random_article',
#'related_posts',
#'share_post',
#'subcategory',
'sitemap',
]

SITEMAP = {
        'format': 'txt',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
            },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
            }
        }

# theme
THEME='../foshuo-theme'
#THEME='pelican-themes/pelican-twitchy'     # with beautifull left navbar
#THEME='pelican-themes/pelican-iliork'      # good for blog, without navbar aside
#THEME='pelican-themes/plumage'             # good for blog, without navbar aside
#THEME='pelican-themes/chunk'               # not very good
#THEME='pelican-themes/elegant'             # red theme
#THEME='pelican-themes/gum'                 # good for blog
#THEME='pelican-themes/Just-Read'
#THEME='pelican-themes/dev-random'

# docutils settings
DOCUTILS_SETTINGS = {}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# tagcloud
TAG_CLOUD_STEPS = 4             # Count of different font sizes in the tag cloud
TAG_CLOUD_MAX_ITEMS = 100       # Maximum number of tags in the cloud

# feed settings
FEED_ATOM = None
FEED_RSS = None
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = None
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#CATEGORY_FEED_RSS = None
#AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
#TAG_FEED_ATOM = None
#TAG_FEED_RSS = None

# url settings
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_ORDER_BY = 'slug'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_ORDER_BY = 'basename'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
#DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'
#SLUG_SUBSTITUTIONS = ()

# for develop
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = True # Uncomment following line if you want document-relative URLs when developing
