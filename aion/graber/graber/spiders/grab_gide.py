##coding=utf-8
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector
#from aion.graber.graber.items import GideItem
#
#class AionGrab(CrawlSpider):
#    name = 'aion'
#    allowed_domains = ['gyrin.com']
#    start_urls = ['http://gyrin.com/']
#    rules = (
#        #Rule(SgmlLinkExtractor(allow='article/\w+'), follow=True),
#        Rule(SgmlLinkExtractor('\d+'), callback='pars_aion', follow=True),)
#
#    def pars_aion(self, response):
#        hxs = HtmlXPathSelector(response)
#        pars = hxs.select('/html/body/table[3]/tr')
#        items = []
#        for elem in pars:
#            item = GideItem()
#            item['title'] = elem.select('td[2]/text()').extract()[0]
#            # item['content'] = elem.select('td[2]/text()').extract()[0]
#            item['content'] = response.url
#            items.append(item)
#        return items
