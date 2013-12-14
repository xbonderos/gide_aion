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
    start_urls = ['http://delovoy-kirov.ru/db']
    rules = (
        #Rule(SgmlLinkExtractor(allow='db-\d+'), follow=True),
        Rule(SgmlLinkExtractor('id\d{3,8}$'), callback='pars_aion', follow=True),)

    def pars_aion(self, response):
        hxs = HtmlXPathSelector(response)
        pars = hxs.select('//*[@id="lt-content"]/div')
        items = []
        for elem in pars:
            item = DkItem()
            item['name'] = elem.select('div[1]/div/span[3]/text()').extract()
            item['address'] = elem.select('table/tr/td[1]/div/div/div[4]/div[1]/div/text()').extract()
            item['email'] = elem.select('table/tr/td[1]/div/div/div[4]/div[3]/span[2]/a/text()').extract()
            item['phone'] = elem.select('table/tr/td[1]/div/div/div[4]/div[2]/div[1]/span/text()').extract()
            item['site'] = elem.select('table/tr/td[1]/div/div/div[4]/div[3]/span[2]/a/text()').extract()
            item['url'] = response.url
            items.append(item)
        return items

