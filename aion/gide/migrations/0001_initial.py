# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pages'
        db.create_table(u'gide_pages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['gide.Pages'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('slug', self.gf('django_autoslug.fields.AutoSlugField')(recursive='parent', populate_from=('title',), max_length=200, blank=True, unique=True, db_index=True)),
            ('cr_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('up_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('content', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'gide', ['Pages'])


    def backwards(self, orm):
        
        # Deleting model 'Pages'
        db.delete_table(u'gide_pages')


    models = {
        u'gide.pages': {
            'Meta': {'ordering': "['title']", 'object_name': 'Pages'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'cr_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['gide.Pages']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'recursive': "'parent'", 'populate_from': "('title',)", 'max_length': '200', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'up_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gide']
