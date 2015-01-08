#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# site settings
AUTHOR = 'Lennyh'
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
DEFAULT_METADATA = (
        ('authors', 'Lennyh'),
        ('lang', 'zh'),
        )

#TEMPLATE_PAGES = {'src/books.html': 'dest/books.html'}

# code highlight options
PYGMENTS_RST_OPTIONS = {
        'linenos':'table',
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
'tipue_search',
#'filetime_from_git',
'neighbors',
#'pdf',
'pin_to_top',
'extract_toc',
#'random_article',
#'related_posts',
#'share_post',
#'subcategory',
'sitemap',
]

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.7,
            'indexes': 0.5,
            'pages': 0.3,
            },
        'changefreqs': {
            'articles': 'daily',
            'indexes': 'daily',
            'pages': 'monthly'
            }
        }

# theme
THEME='../foshuo-theme'
#THEME='pelican-themes/elegant'             # red theme

# docutils settings
DOCUTILS_SETTINGS = {}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

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

# Social widget
SOCIAL = (('github', 'https://github.com/lennyhbt'),
          )

SOHU_CHANGYAN = True
SHARELINK = "bottom"

# elegant settings
# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
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
TAG_URL = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'保持联系'
RELATED_POSTS_LABEL = '继续阅读...'

# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> 佛说</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://lennyhbt.github.io/" property="cc:attributionName" rel="cc:attributionURL">Lennyhbt</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'My name is Talha Mansoor \u2015 a software engineer who gets things done. I am talha131 at Github and @talham_ at twitter. I design and build software products for iOS and OSX. I work on Jump Desktop which is a remote desktop application for iOS, OSX and Android. This is my personal blog.'

# Landing Page
PROJECTS = [
{
'name': 'Big-Doc',
'url':
'https://github.com/lennyhbt/big-doc',
'description': '自己所写及所译的一些技术文档'},
]
LANDING_PAGE_ABOUT = {'title': '佛说',
'details': """
关于我，关于本站，确实没有太多要说的，大家看就好了:)
"""}

# for develop
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = True # Uncomment following line if you want document-relative URLs when developing

