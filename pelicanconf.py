#!/usr/bin/env python
## http://docs.getpelican.com/en/latest/settings.html

SITENAME = 'Roblog'
AUTHOR = 'Rob Schaber'
SITEURL = 'http://robschaber.com'
DEFAULT_LANG = 'en'
LOCALE = 'C'
TIMEZONE = 'America/Chicago'

PATH = 'src/'
OUTPUT_PATH = 'out/'

## http://docs.getpelican.com/en/latest/themes.html
## https://github.com/getpelican/pelican-themes

THEME = 'pelican-themes/chunk' # built-in: (notmyidea,simple)
# THEME_STATIC_DIR = 'theme'
# THEME_STATIC_PATHS = ['static']
# CSS_FILE = 'main.css'

# STATIC_PATHS = ['pictures','extra/robots.txt']

DIRECT_TEMPLATES = ['index','categories','tags']
# PAGINATED_DIRECT_TEMPLATES = ['index']

PAGE_PATHS = ['page']
PAGE_EXCLUDES = []
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

ARTICLE_PATHS = ['post']
ARTICLE_EXCLUDES = []
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'

DRAFT_PATHS = ['draft']
DRAFT_EXCLUDES = []
DRAFT_SAVE_AS = '{slug}/index.html'
DRAFT_URL = '{slug}/'

TAG_SAVE_AS = '{slug}/index.html'
TAG_URL = '{slug}/'

CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'

AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''

ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''


# SLUG_SUBSTITUTIONS = ()

TYPOGRIFY = False
# TYPOGRIFY_IGNORE_TAGS = ['pre','code']

CACHE_PATH = 'cache'
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
GZIP_CACHE = True
# CONTENT_CACHING_LAYER = 'reader'  # (reader,generator)

DELETE_OUTPUT_DIRECTORY = True
# LOG_FILTER = [(logging.WARN, 'TAG_SAVE_AS is set to False')]

RELATIVE_URLS = True
OUTPUT_SOURCES = False

# TEMPLATE_PAGES = {'one/page.html': 'two/page.html'}
# EXTRA_TEMPLATES_PATHS = []

SLUGIFY_SOURCE = 'basename'
SUMMARY_MAX_LENGTH = 0
DEFAULT_PAGINATION = False
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
CHECK_MODIFIED_METHOD = 'md5'  # (mtime,md5)

TAG_CLOUD_STEPS = 3
TAG_CLOUD_MAX_ITEMS = 50

DEFAULT_CATEGORY = 'Posts'
USE_FOLDER_AS_CATEGORY = False

# INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'

# DEFAULT_METADATA = (('yeah', 'it is'),)
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2}).*)'
# PATH_METADATA = ''
# EXTRA_PATH_METADATA = {
# 	'extra/robots.txt': {'path': 'robots.txt'},
# }

## http://pythonhosted.org/Markdown/extensions/
# MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']


## SETTINGS USED BY DEFAULT THEME
SITESUBTITLE = 'site subtitle'
DISQUS_SITENAME = ''
GITHUB_URL = ''
TWITTER_USERNAME = ''
GOOGLE_ANALYTICS = ''
GOSQUARED_SITENAME = ''
# MENUITEMS = [('title','url'),('title2','url2')]
PIWIK_URL = ''
PIWIK_SSL_URL = ''
PIWIK_SITE_ID = ''

# LINKS = (
# 	('Biologeek', 'http://biologeek.org'),
# 	('Filyb', 'http://filyb.info/'),
# 	('Libert-fr', 'http://www.libert-fr.com'),
# 	('N1k0', 'http://prendreuncafe.com/blog/'),
# 	('Zubin Mithra', 'http://zubin71.wordpress.com/'),
# )

# SOCIAL = (
# 	('twitter', 'http://twitter.com/ametaireau'),
# 	('lastfm', 'http://lastfm.com/user/akounet'),
# 	('github', 'http://github.com/ametaireau'),
# )


# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True

# PDF_GENERATOR = False

# JINJA_EXTENSIONS = []
# JINJA_FILTERS = {}
# READERS = {}


FEED_DOMAIN = SITEURL
# FEED_MAX_ITEMS = 50

FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
AUTHOR_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_RSS = 'rss.xml'
FEED_ALL_RSS = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = None
TRANSLATION_FEED_RSS = None





## http://docs.getpelican.com/en/latest/plugins.html

# PLUGINS = []
# PLUGIN_PATHS = []
