# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'ShowMeta'
        db.create_table('show_meta', (
            ('id', self.gf('django.db.models.fields.AutoField')(max_length=255, db_column='id', primary_key=True)),
            ('show_title', self.gf('django.db.models.fields.TextField')(db_column='show_title')),
            ('watch_count', self.gf('django.db.models.fields.IntegerField')(db_column='watch_count')),
            ('likes', self.gf('django.db.models.fields.IntegerField')(db_column='likes')),
        ))
        db.send_create_signal('series', ['ShowMeta'])

        # Adding model 'MovieMeta'
        db.create_table('movie_meta', (
            ('id', self.gf('django.db.models.fields.AutoField')(max_length=255, db_column='id', primary_key=True)),
            ('movie_title', self.gf('django.db.models.fields.TextField')(db_column='movie_title')),
            ('watch_count', self.gf('django.db.models.fields.IntegerField')(db_column='watch_count')),
            ('likes', self.gf('django.db.models.fields.IntegerField')(db_column='likes')),
        ))
        db.send_create_signal('series', ['MovieMeta'])

        # Adding model 'NewShow'
        db.create_table('new_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(db_column='id', primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')(db_column='title')),
            ('description', self.gf('django.db.models.fields.TextField')(db_column='description')),
            ('image', self.gf('django.db.models.fields.TextField')(db_column='image')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='date', auto_now=True, blank=True)),
        ))
        db.send_create_signal('series', ['NewShow'])

        # Adding model 'NewEpisode'
        db.create_table('new_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(db_column='id', primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')(db_column='title')),
            ('link', self.gf('django.db.models.fields.TextField')(db_column='link')),
            ('show_title', self.gf('django.db.models.fields.TextField')(db_column='show_title')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='date', auto_now=True, blank=True)),
        ))
        db.send_create_signal('series', ['NewEpisode'])

        # Adding model 'NewMovie'
        db.create_table('new_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(db_column='id', primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')(db_column='title')),
            ('description', self.gf('django.db.models.fields.TextField')(db_column='description')),
            ('image', self.gf('django.db.models.fields.TextField')(db_column='image')),
            ('genera', self.gf('django.db.models.fields.TextField')(db_column='genera')),
            ('frame', self.gf('django.db.models.fields.TextField')(db_column='frame')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='date', auto_now=True, blank=True)),
        ))
        db.send_create_signal('series', ['NewMovie'])


    def backwards(self, orm):
        # Deleting model 'ShowMeta'
        db.delete_table('show_meta')

        # Deleting model 'MovieMeta'
        db.delete_table('movie_meta')

        # Deleting model 'NewShow'
        db.delete_table('new_show')

        # Deleting model 'NewEpisode'
        db.delete_table('new_episode')

        # Deleting model 'NewMovie'
        db.delete_table('new_movie')


    models = {
        'series.moviemeta': {
            'Meta': {'object_name': 'MovieMeta', 'db_table': "'movie_meta'"},
            'id': (
                'django.db.models.fields.AutoField', [],
                {'max_length': '255', 'db_column': "'id'", 'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'db_column': "'likes'"}),
            'movie_title': ('django.db.models.fields.TextField', [], {'db_column': "'movie_title'"}),
            'watch_count': ('django.db.models.fields.IntegerField', [], {'db_column': "'watch_count'"})
        },
        'series.newepisode': {
            'Meta': {'object_name': 'NewEpisode', 'db_table': "'new_episode'"},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'db_column': "'link'"}),
            'show_title': ('django.db.models.fields.TextField', [], {'db_column': "'show_title'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        },
        'series.newmovie': {
            'Meta': {'object_name': 'NewMovie', 'db_table': "'new_movie'"},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'frame': ('django.db.models.fields.TextField', [], {'db_column': "'frame'"}),
            'genera': ('django.db.models.fields.TextField', [], {'db_column': "'genera'"}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'db_column': "'image'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        },
        'series.newshow': {
            'Meta': {'object_name': 'NewShow', 'db_table': "'new_show'"},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'db_column': "'image'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        },
        'series.showmeta': {
            'Meta': {'object_name': 'ShowMeta', 'db_table': "'show_meta'"},
            'id': (
                'django.db.models.fields.AutoField', [],
                {'max_length': '255', 'db_column': "'id'", 'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'db_column': "'likes'"}),
            'show_title': ('django.db.models.fields.TextField', [], {'db_column': "'show_title'"}),
            'watch_count': ('django.db.models.fields.IntegerField', [], {'db_column': "'watch_count'"})
        }
    }

    complete_apps = ['series']