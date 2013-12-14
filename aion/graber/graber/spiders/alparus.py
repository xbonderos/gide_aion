##coding=utf-8
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector
#from aion.graber.graber.items import AlParus
#
#
#class Gid43(CrawlSpider):
#    name = 'parus'
#    allowed_domains = ['daichi.ru']
#    start_urls = ['http://daichi.ru/catalog'
#                  ]
#    rules = (
#        #Rule(SgmlLinkExtractor(allow='catalog/\[a-z]/\[a-z]'), follow=True),
#        Rule(SgmlLinkExtractor('catalog/\w+/\w+/item/\d{3,8}/\d{3,8}'), callback='pars_aion', follow=True),)
#
#    def pars_aion(self, response):
#        hxs = HtmlXPathSelector(response)
#        pars = hxs.select('//div[@id="comp_94feb9fe757594b68a12d31f9d75c5e6"]')
#        items = []
#        for elem in pars:
#            item = AlParus()
#            item['name'] = elem.select('div[2]/h1/text()').extract()[0].encode('utf-8')
#            item['content'] = elem.select('div[4]/div/div[1]').extract()
#            #item['img'] = elem.select('//*[@id="picture"]/img').extract()[0]
#            item['url'] = response.url
#            items.append(item)
#        return items
#
