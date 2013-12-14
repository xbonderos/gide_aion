#coding=utf-8
from django.conf.urls import *
#from hitcount.views import update_hit_count_ajax

urlpatterns = patterns('aion.gide.views',
                       url(r'^(?P<slug>.+)/$', 'detail', name='detail'),
                       url(r'^$', 'main', name='main'),
                       #url(r'^ajax/hit/$', update_hit_count_ajax, name='hitcount_update_ajax'),
                       url(r'^tags/$', 'list_tags'),

)
