# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Pages.img'
        db.alter_column(u'gide_pages', 'img', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'Pages.img'
        db.alter_column(u'gide_pages', 'img', self.gf('django.db.models.fields.files.ImageField')(max_length=100))


    models = {
        u'gide.pages': {
            'Meta': {'ordering': "['title']", 'object_name': 'Pages'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'cr_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['gide.Pages']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'recursive': "'parent'", 'populate_from': "('title',)", 'max_length': '200', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'up_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gide']
