# coding=utf-8
import random
import base64
from scrapy import log
import telnetlib
from scrapy.contrib.downloadermiddleware.redirect import RedirectMiddleware
import time


class ProxyMiddleware(object):
    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        proxy_list = self.settings.get("PROXY_LIST")
        proxy = random.choice(proxy_list)
        request.meta['proxy'] = proxy['address']
        if proxy['auth'] is not None:
            encoded_user_pass = base64.encodestring(proxy['auth'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass


class TorControl(object):
    def get_new_ip(self):
        #tn = telnetlib.Telnet('127.0.0.1', 9050)
        #tn.read_until("Escape character is '^]'.", 2)
        #tn.write('AUTHENTICATE\r\n')
        #tn.read_until("250 OK", 2)
        #tn.write("signal NEWNYM\r\n")
        #tn.read_until("250 OK", 2)
        ##time.sleep(3)
        #tn.write("quit\r\n")
        #tn.close()

        log.msg("inside the tor change proxy function")
        log.msg('Changing proxy')
        print "Changing Proxy"
        tn = telnetlib.Telnet('127.0.0.1', 9050)
        tn.read_until("Escape character is '^]'.", 2)
        tn.write('AUTHENTICATE\r\n')
        tn.read_until("250 OK", 2)
        tn.write("signal NEWNYM\r\n")
        tn.read_until("250 OK", 2)
        time.sleep(5)
        tn.write("quit\r\n")
        tn.close()
        time.sleep(2)


class TorProxyMiddleware(TorControl, ProxyMiddleware):
    def process_exception(self, request, exception, spider):
        log.msg(u'New IP in Tor')
        try:
            self.get_new_ip()
        except ValueError:
            pass


class TorRedirectMiddleware(TorControl, RedirectMiddleware):
    def _redirect(self, redirected, request, spider, reason):
        ttl = request.meta.setdefault('redirect_ttl', self.max_redirect_times)
        redirects = request.meta.get('redirect_times', 0) + 1

        if ttl and redirects <= self.max_redirect_times:
            if redirects % 2 == 0:
                self.get_new_ip()

            redirected.meta['redirect_times'] = redirects
            redirected.meta['redirect_ttl'] = ttl - 1
            redirected.meta['redirect_urls'] = request.meta.get('redirect_urls', []) + [request.url]
            redirected.dont_filter = request.dont_filter
            redirected.priority = request.priority + self.priority_adjust
            log.msg(format="Redirecting (%(reason)s) to %(redirected)s from %(request)s",
                    level=log.DEBUG, spider=spider, request=request,
                    redirected=redirected, reason=reason)
            return redirected
        else:
            log.msg(format="Discarding %(request)s: max redirections reached",
                    level=log.DEBUG, spider=spider, request=request)
            self.get_new_ip()
