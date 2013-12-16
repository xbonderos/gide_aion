#coding=utf-8
from django.db import models
from django_autoslug.fields import AutoSlugField
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from tagging.fields import TagField
from tagging.models import Tag
from sorl.thumbnail import ImageField


class Pages(MPTTModel):
    STATUS_DRAFT = 1
    STATUS_PUB = 2

    STATUS_PUBLIC = [
        (STATUS_DRAFT, u'Скрыто'),
        (STATUS_PUB, u'Опубликовано'),
    ]
    title = models.CharField(max_length=150, verbose_name=u'Заголовок')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='Родитель')
    status = models.IntegerField(u'Статус', choices=STATUS_PUBLIC, default=STATUS_PUB)
    slug = AutoSlugField(populate_from=('title',), recursive='parent', unique=True, max_length=200, overwrite=True)
    cr_date = models.DateField(auto_now_add=True)
    up_date = models.DateField(auto_now=True)
    img = ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
    content = HTMLField(blank=True)
    tags = TagField()
    #я тут что то изменил
    class Seo:
        populate = {
            'title': 'title',
            'keywords': 'content',
            'description': 'content'
        }


    class Meta:
        ordering = ["title"]
        verbose_name = 'Гайд'
        verbose_name_plural = 'Гайды'


    class MPTTMeta:
        order_insertion_by = ['title']
        parent_attr = 'parent'


    def __unicode__(self):
        return self.title

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)


    def short_content(self):
        if self.content.find('<!-- pagebreak -->') > -1:
            return self.content[:self.content.find('<!-- pagebreak -->')]
        else:
            return self.content[:200]

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {'slug': self.slug})


#from ratings.handlers import ratings
#from ratings.forms import SliderVoteForm
#
#ratings.register(Pages, score_range=(1, 5), form_class=SliderVoteForm)

mptt.register(Pages, )
