# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'equiz_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'equiz', ['Category'])

        # Adding model 'Section'
        db.create_table(u'equiz_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sections', to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equiz.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'equiz', ['Section'])

        # Adding model 'QuestionType'
        db.create_table(u'equiz_questiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'equiz', ['QuestionType'])

        # Adding model 'Question'
        db.create_table(u'equiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equiz.QuestionType'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equiz.Section'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('markerTime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('replayTime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('penalty', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('feedback', self.gf('django.db.models.fields.CharField')(default='Correct', max_length=300, blank=True)),
            ('hint', self.gf('django.db.models.fields.CharField')(default='Incorrect', max_length=300, blank=True)),
        ))
        db.send_create_signal(u'equiz', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'equiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['equiz.Question'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('is_answer_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'equiz', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'equiz_category')

        # Deleting model 'Section'
        db.delete_table(u'equiz_section')

        # Deleting model 'QuestionType'
        db.delete_table(u'equiz_questiontype')

        # Deleting model 'Question'
        db.delete_table(u'equiz_question')

        # Deleting model 'Answer'
        db.delete_table(u'equiz_answer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'equiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_answer_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['equiz.Question']"})
        },
        u'equiz.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'equiz.question': {
            'Meta': {'object_name': 'Question'},
            'feedback': ('django.db.models.fields.CharField', [], {'default': "'Correct'", 'max_length': '300', 'blank': 'True'}),
            'hint': ('django.db.models.fields.CharField', [], {'default': "'Incorrect'", 'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markerTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'penalty': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'quiz_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equiz.QuestionType']"}),
            'replayTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equiz.Section']"}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'})
        },
        u'equiz.questiontype': {
            'Meta': {'object_name': 'QuestionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'equiz.section': {
            'Meta': {'object_name': 'Section'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equiz.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['equiz']