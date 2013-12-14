##coding=utf-8
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector
#from aion.graber.graber.items import GidMail
#
#
#class Gid43(CrawlSpider):
#    name = 'gid'
#    allowed_domains = ['www.gid43.ru']
#    start_urls = ['http://www.gid43.ru/rubric/full/id/184107503']
#    rules = (
#        #Rule(SgmlLinkExtractor(allow='firm/id'), follow=True),
#        Rule(SgmlLinkExtractor('firm/id/\d{1,4}/'), callback='pars_aion', follow=True),)
#
#    def pars_aion(self, response):
#        hxs = HtmlXPathSelector(response)
#        pars = hxs.select('//*[@id="content-area"]/div[1]/div/div[3]/div[2]')
#        items = []
#        for elem in pars:
#            item = GidMail()
#            item['name'] = elem.select('h1/text()').extract()[0]
#            item['mail'] = elem.select('div[7]/text()').extract()[0]
#            item['adres'] = elem.select('div[5]/text()').extract()[0]
#            items.append(item)
#        return items
#
#    #hxs.select('//*[@id="content-area"]/div[1]/div/div[3]/div[@id="firm-email"]/text()').extract()[0]
#    #//*[@id="content-area"]/div[1]/div/div[3]/div[2]/h1
#    #//*[@id="content-area"]/div[1]/div/div[3]/div[2]/div[7]
#    #//*[@id="content-area"]/div[1]/div/div[3]/div[2]/div[5]
#    #//*[@id="lt-content"]/div/table/tbody/tr/td[1]/div/div/div[3]/div[1]/div[2]/div[3]/span[2]/a