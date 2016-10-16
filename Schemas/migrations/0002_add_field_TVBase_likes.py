# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'TVBase.likes'
        db.add_column('Schemas_tvbase', 'likes',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TVBase.likes'
        db.delete_column('Schemas_tvbase', 'likes')


    models = {
        'Schemas.actor': {
            'Meta': {'_ormbases': ['Schemas.Person'], 'object_name': 'Actor'},
            'person_id': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'unique': 'True', 'to': "orm['Schemas.Person']", 'primary_key': 'True'})
        },
        'Schemas.aggregaterating': {
            'Meta': {'object_name': 'AggregateRating'},
            'bestRating': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemReviewed': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'ratingCount': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'ratingValue': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'reviewCount': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'worstRating': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'})
        },
        'Schemas.country': {
            'Meta': {'object_name': 'Country'},
            'globalLocationNumber': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'logo': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'})
        },
        'Schemas.episode': {
            'Meta': {'object_name': 'Episode'},
            'episodeNumber': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'new_episode': ('django.db.models.fields.related.OneToOneField', [],
                            {'unique': 'True', 'null': 'True', 'to': "orm['series.NewEpisode']", 'default': 'None',
                             'blank': 'True'}),
            'partOfSeason': ('django.db.models.fields.related.ForeignKey', [],
                             {'null': 'True', 'to': "orm['Schemas.Season']", 'default': 'None', 'blank': 'True'}),
            'partOfSeries': ('django.db.models.fields.related.ForeignKey', [],
                             {'null': 'True', 'to': "orm['Schemas.TVSeries']", 'default': 'None', 'blank': 'True'}),
            'subtitle_rating': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'views': ('django.db.models.fields.related.ManyToManyField', [],
                      {'null': 'True', 'symmetrical': 'False', 'default': 'None', 'to': "orm['Schemas.View']",
                       'blank': 'True'})
        },
        'Schemas.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'Schemas.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.TextField', [], {'null': 'True', 'default': 'None', 'blank': 'True'})
        },
        'Schemas.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.SlugField', [],
                    {'null': 'True', 'default': 'None', 'blank': 'True', 'max_length': '50'})
        },
        'Schemas.movie': {
            'Meta': {'_ormbases': ['Schemas.TVBase'], 'object_name': 'Movie'},
            'imdb': ('django.db.models.fields.related.OneToOneField', [],
                     {'unique': 'True', 'null': 'True', 'to': "orm['imdb.Movies']", 'default': 'None',
                      'blank': 'True'}),
            'is_czech': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'new_movie': ('django.db.models.fields.related.OneToOneField', [],
                          {'unique': 'True', 'null': 'True', 'to': "orm['series.NewMovie']", 'default': 'None',
                           'blank': 'True'}),
            'tvbase_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'unique': 'True', 'to': "orm['Schemas.TVBase']", 'primary_key': 'True'})
        },
        'Schemas.musicgroup': {
            'Meta': {'object_name': 'MusicGroup', 'db_table': "'music_group_schema'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'})
        },
        'Schemas.organization': {
            'Meta': {'object_name': 'Organization'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'null': 'True', 'default': 'None', 'blank': 'True', 'max_length': '200'})
        },
        'Schemas.person': {
            'Meta': {'object_name': 'Person'},
            'birthDate': (
                'django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'deathDate': (
                'django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'duns': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'gender': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [],
                            {'null': 'True', 'to': "orm['Schemas.Country']", 'default': 'None', 'blank': 'True'}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'null': 'True', 'default': 'None', 'blank': 'True', 'max_length': '200'})
        },
        'Schemas.rating': {
            'Meta': {'object_name': 'Rating'},
            'bestRating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratingValue': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'worstRating': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'Schemas.review': {
            'Meta': {'object_name': 'Review'},
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'null': 'True', 'symmetrical': 'False', 'default': 'None',
                                  'to': "orm['Schemas.AggregateRating']", 'blank': 'True'}),
            'dateCreated': (
                'django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'date_reviewed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'default': "'CS cz'", 'max_length': '100'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'itemReviewed': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [],
                         {'null': 'True', 'symmetrical': 'False', 'default': 'None', 'to': "orm['Schemas.Keyword']",
                          'blank': 'True'}),
            'reviewBody': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'reviewRating': ('django.db.models.fields.related.OneToOneField', [],
                             {'unique': 'True', 'null': 'True', 'to': "orm['Schemas.Rating']", 'default': 'None',
                              'blank': 'True'})
        },
        'Schemas.season': {
            'Meta': {'object_name': 'Season'},
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'numberOfEpisodes': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'partOfSeries': ('django.db.models.fields.related.ForeignKey', [],
                             {'null': 'True', 'to': "orm['Schemas.TVSeries']", 'default': 'None', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'})
        },
        'Schemas.tvbase': {
            'Meta': {'object_name': 'TVBase'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [],
                       {'related_name': "'actors'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                        'default': 'None', 'to': "orm['Schemas.Person']"}),
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'related_name': "'ratings'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                                  'default': 'None', 'to': "orm['Schemas.AggregateRating']"}),
            'alternateName': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'cinematographers': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'related_name': "'cinematographers'", 'symmetrical': 'False', 'blank': 'True',
                                  'null': 'True', 'default': 'None', 'to': "orm['Schemas.Person']"}),
            'datePublished': (
                'django.db.models.fields.DateTimeField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [],
                         {'related_name': "'directors'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                          'default': 'None', 'to': "orm['Schemas.Person']"}),
            'distributors': ('django.db.models.fields.related.ManyToManyField', [],
                             {'related_name': "'distributors'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                              'default': 'None', 'to': "orm['Schemas.Organization']"}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [],
                      {'null': 'True', 'symmetrical': 'False', 'default': 'None', 'to': "orm['Schemas.Genre']",
                       'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [],
                       {'related_name': "'image_group'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                        'default': 'None', 'to': "orm['Schemas.Image']"}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'default': "'Cs cz'", 'max_length': '200'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'isFamilyFriendly': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [],
                         {'null': 'True', 'symmetrical': 'False', 'default': 'None', 'to': "orm['Schemas.Keyword']",
                          'blank': 'True'}),
            'likes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'musicBy': ('django.db.models.fields.related.ManyToManyField', [],
                        {'related_name': "'musician'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                         'default': 'None', 'to': "orm['Schemas.Person']"}),
            'musicByGroup': ('django.db.models.fields.related.ManyToManyField', [],
                             {'related_name': "'music_group'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                              'default': 'None', 'to': "orm['Schemas.MusicGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'numberOfEpisodes': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'producer': ('django.db.models.fields.related.ManyToManyField', [],
                         {'related_name': "'producer'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                          'default': 'None', 'to': "orm['Schemas.Person']"}),
            'production_companies': ('django.db.models.fields.related.ManyToManyField', [],
                                     {'related_name': "'production_companies'", 'symmetrical': 'False', 'blank': 'True',
                                      'null': 'True', 'default': 'None', 'to': "orm['Schemas.Organization']"}),
            'review': ('django.db.models.fields.related.ManyToManyField', [],
                       {'null': 'True', 'symmetrical': 'False', 'default': 'None', 'to': "orm['Schemas.Review']",
                        'blank': 'True'}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'null': 'True', 'default': 'None', 'blank': 'True', 'max_length': '200'}),
            'videoObject': ('django.db.models.fields.related.ManyToManyField', [],
                            {'null': 'True', 'symmetrical': 'False', 'default': 'None',
                             'to': "orm['Schemas.VideoObject']", 'blank': 'True'}),
            'views': ('django.db.models.fields.related.ManyToManyField', [],
                      {'null': 'True', 'symmetrical': 'False', 'default': 'None', 'to': "orm['Schemas.View']",
                       'blank': 'True'}),
            'writers': ('django.db.models.fields.related.ManyToManyField', [],
                        {'related_name': "'writers'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True',
                         'default': 'None', 'to': "orm['Schemas.Person']"})
        },
        'Schemas.tvseries': {
            'Meta': {'_ormbases': ['Schemas.TVBase'], 'object_name': 'TVSeries'},
            'imdb': ('django.db.models.fields.related.OneToOneField', [],
                     {'unique': 'True', 'null': 'True', 'to': "orm['imdb.Movies']", 'default': 'None',
                      'blank': 'True'}),
            'new_show': ('django.db.models.fields.related.OneToOneField', [],
                         {'unique': 'True', 'null': 'True', 'to': "orm['series.NewShow']", 'default': 'None',
                          'blank': 'True'}),
            'tvbase_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'unique': 'True', 'to': "orm['Schemas.TVBase']", 'primary_key': 'True'})
        },
        'Schemas.videoobject': {
            'Meta': {'object_name': 'VideoObject'},
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'null': 'True', 'symmetrical': 'False', 'default': 'None',
                                  'to': "orm['Schemas.AggregateRating']", 'blank': 'True'}),
            'embedUrl': ('django.db.models.fields.TextField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'encodingFormat': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'default': "'CS cz'", 'max_length': '100'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'productionCompany': ('django.db.models.fields.related.ManyToManyField', [],
                                  {'null': 'True', 'symmetrical': 'False', 'default': 'None',
                                   'to': "orm['Schemas.Organization']", 'blank': 'True'}),
            'uploadDate': (
                'django.db.models.fields.DateTimeField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'videoFrameSize': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'videoQuality': (
                'django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'})
        },
        'Schemas.view': {
            'Meta': {'object_name': 'View'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'view_count': ('django.db.models.fields.BigIntegerField', [], {}),
            'view_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'imdb.movies': {
            'Meta': {'object_name': 'Movies', 'db_table': "'movies'"},
            'imdbid': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10'}),
            'movieid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'year': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'})
        },
        'series.newepisode': {
            'Meta': {'object_name': 'NewEpisode', 'db_table': "'new_episode'"},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'auto_now': 'True', 'db_column': "'date'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'db_column': "'link'"}),
            'show_title': ('django.db.models.fields.TextField', [], {'db_column': "'show_title'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        },
        'series.newmovie': {
            'Meta': {'object_name': 'NewMovie', 'db_table': "'new_movie'"},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'auto_now': 'True', 'db_column': "'date'", 'blank': 'True'}),
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
                {'auto_now': 'True', 'db_column': "'date'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'db_column': "'image'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        }
    }

    complete_apps = ['Schemas']