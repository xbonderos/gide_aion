from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field, Item
from aion.theft.models import Dk


#class GideItem(DjangoItem):
#    django_model = Pages
#

#class GidMail(Item):
#    name = Field()
#    mail = Field()
#    adres = Field()


#class AlParus(Item):
#    name = Field()
#    content = Field()
#    #img = Field()
#    url = Field()

class DkItem(DjangoItem):
    django_model = Dk


