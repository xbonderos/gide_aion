from aion.gide.models import Pages
from aion.theft.models import Dk

class DjangoPipeline(object):
    def process_item(self, item, spider):
        item = Dk(
            name=item['name'],
            address=item['address'],
            email=item['email'],
            phone=item['phone'],
            site=item['site'],
            url=item['url'],
            )
        item.save()
        return item

#class DjangoPipelineGid(object):
#    def process_item(self, item, spider):
#        item = GidMail(
#            name=item['name'],
#            mail=item['mail'],
#            adres=item['adres'],
#        )
#        return item

#class DjangoPipelineParus(object):
#    def process_item(self, item, spider):
#        item = AlParus(
#            name=item['name'],
#            content=item['content'],
#            url=item['url'],
#        )
#        return item