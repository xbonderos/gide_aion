#coding=utf-8
from django.contrib import admin
from feincms.admin import tree_editor
from django.utils.translation import gettext_lazy as _
from aion.gide.models import Pages
from mce_filebrowser.admin import MCEFilebrowserAdmin
from seo107.admin import SeoAdminMixin

try:
    from seo107.admin import SeoAdminMixin
except ImportError:
    class SeoAdminMixin(object):
        pass


class PagesAdminModel(SeoAdminMixin, tree_editor.TreeEditor, MCEFilebrowserAdmin):
    list_display = ('title', 'img', 'cr_date', 'status',)
    active_toggle = tree_editor.ajax_editable_boolean('active', _('active'))
    actions = ['status']
    fields = ('title', 'img', ('parent', 'status', ), 'content')


admin.site.register(Pages, PagesAdminModel)
