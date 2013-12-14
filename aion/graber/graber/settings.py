ITEM_PIPELINES = [
    'aion.graber.graber.pipelines.DjangoPipeline',
    # 'aion.graber.graber.pipelines.DjangoPipelineGid',
    # 'aion.graber.graber.pipelines.DjangoPipelineParus',
]

BOT_NAME = 'graber'

SPIDER_MODULES = ['graber.spiders']
NEWSPIDER_MODULE = 'graber.spiders'

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7', ]

PROXY_LIST = [
    {'address': 'http://127.0.0.1:8118', 'auth': 'None'},
    #{'address': 'http://127.0.0.1:9050', 'auth': 'None'},
    # {'address': 'http://127.0.0.1:9000', 'auth': 'None'},
    #{'address': 'http://127.0.0.1:9150', 'auth': 'None'},

]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': None,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'graber.middleware.proxy.TorRedirectMiddleware': 390,
    'graber.middleware.useragent.RandomUserAgentMiddleware': 400,
    'graber.middleware.proxy.TorProxyMiddleware': 410,
    'graber.middleware.proxy.TorControl': 600,

}
#/Users/user/venv/aion/aion/graber/graber/Middleware/proxy.py
#import os
#LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs', 'all.logs')



def setup_django_env(path):
    import os, imp
    import sys
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)
    setup_environ(project)
    sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))


setup_django_env('/Users/user/venv/aion/aion/')
