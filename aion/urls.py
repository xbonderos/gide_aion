#coding=utf-8
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from filebrowser.sites import site
from hitcount.views import update_hit_count_ajax


admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/filebrowser/', include(site.urls)),
                       url(r'^tinymce/', include('tinymce.urls')),
                       url(r'^tracking/', include('tracking.urls')),
                       url(r'^count/', include('django_counter.urls')),
                       url(r'^', include('aion.gide.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
