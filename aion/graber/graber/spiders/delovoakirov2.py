#coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from aion.graber.graber.items import DkItem

import logging
from scrapy.log import ScrapyFileLogObserver

logfile = open('testlog.logs', 'w')
log_observer = ScrapyFileLogObserver(logfile, level=logging.DEBUG)
log_observer.start()


class DkParse(CrawlSpider):
    name = 'dk'
    allowed_domains = ['delovoy-kirov.ru']
    start_urls = ['http://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%83%D0%BB%D0%B8%D1%86_%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D0%B0']
    rules = (
        #Rule(SgmlLinkExtractor(allow='db-\d+'), follow=True),
        Rule(SgmlLinkExtractor('id\d{3,8}$'), callback='pars_aion', follow=True),)

    def pars_aion(self, response):
        hxs = HtmlXPathSelector(response)
        pars = hxs.select('//*[@id="mw-content-text"]/table[2]/tr')
        items = []
        for elem in pars:
            item = DkItem()
            item['name'] = elem.select('td[2]/text()').extract()
            items.append(item)
        return items

