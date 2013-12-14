from django.contrib import admin
from aion.pageviews.models import HitCount


class HitCountAdmin(admin.ModelAdmin):
	list_display = ('url', 'hits')


admin.site.register(HitCount, HitCountAdmin)
