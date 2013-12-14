import os

ROOT_PATH = os.path.dirname(__file__)

DJANGO_SETTINGS_MODULE = 'aion.settings'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'aion', # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = os.path.join(ROOT_PATH, '/media/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = os.path.join(ROOT_PATH, '/static/')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'dev_static/'),
)
ADMIN_MEDIA_PREFIX = '/media/'
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q07awbx-pfnvmlr+d&_%kh9$5fsmi1-x-_&_efuh*v9uj*x5x-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'aion.pageviews.middleware.PageViewsMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aion.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'aion.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)
INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS = (
    #'grappelli',
    'debug_toolbar',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'crumbs',
    #'ratings', #django-generic-ratings
    'tagging',
    'mptt',
    'south',
    'pytils',
    'sorl.thumbnail',

    'aion.gide',
    #'aion.pageviews',

    'django_counter',

    'hitcount',
    'tinymce',
    'sorl.thumbnail',
    'filebrowser',
    'feincms',
    'seo107',
    'endless_pagination',
    'tracking',
)
THUMBNAIL_PREFIX = 'cache/'
TRACK_AJAX_REQUESTS = False
TRACK_ANONYMOUS_USERS = True
TRACK_PAGEVIEWS = True

from django.template import add_to_builtins

add_to_builtins('django.templatetags.i18n')

TINYMCE_DEFAULT_CONFIG = {
    'file_browser_callback': 'filebrowser',
    'plugins': 'pagebreak,advimage,advlink,table,searchreplace,contextmenu,template,paste,save,autosave,media',
    'themes': 'advanced',
    'lange': 'ru',
    'theme_advanced_buttons1': "pagebreak,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,"
                               "formatselect,fontsizeselect,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,"
                               "link,unlink,anchor,image,cleanup,help,code,|,forecolor",
    'theme_advanced_buttons2': "tablecontrols,|,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolba  r_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'width': 950,
    'height': 500,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'seo107.context_processors.seo',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
