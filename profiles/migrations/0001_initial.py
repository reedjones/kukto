# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('profiles_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('active_int', self.gf('django.db.models.fields.BigIntegerField')(default=1)),
            ('picture',
             self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100, default=None)),
        ))
        db.send_create_signal('profiles', ['UserProfile'])

        # Adding M2M table for field liked_series on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_liked_series')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('tvseries', models.ForeignKey(orm['Schemas.tvseries'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'tvseries_id'])

        # Adding M2M table for field liked_movies on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_liked_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('movie', models.ForeignKey(orm['Schemas.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'movie_id'])

        # Adding M2M table for field liked_episodes on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_liked_episodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('episode', models.ForeignKey(orm['Schemas.episode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'episode_id'])

        # Adding M2M table for field watched_series on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_watched_series')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('tvseries', models.ForeignKey(orm['Schemas.tvseries'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'tvseries_id'])

        # Adding M2M table for field watched_movies on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_watched_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('movie', models.ForeignKey(orm['Schemas.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'movie_id'])

        # Adding M2M table for field watched_episodes on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_watched_episodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('episode', models.ForeignKey(orm['Schemas.episode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'episode_id'])

        # Adding M2M table for field rated_series on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_rated_series')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('tvseries', models.ForeignKey(orm['Schemas.tvseries'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'tvseries_id'])

        # Adding M2M table for field rated_movies on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_rated_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('movie', models.ForeignKey(orm['Schemas.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'movie_id'])

        # Adding M2M table for field rated_episodes on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_rated_episodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('episode', models.ForeignKey(orm['Schemas.episode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'episode_id'])

        # Adding M2M table for field reviewed_series on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_reviewed_series')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('tvseries', models.ForeignKey(orm['Schemas.tvseries'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'tvseries_id'])

        # Adding M2M table for field reviewed_movies on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_reviewed_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('movie', models.ForeignKey(orm['Schemas.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'movie_id'])

        # Adding M2M table for field reviewed_episodes on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_reviewed_episodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('episode', models.ForeignKey(orm['Schemas.episode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'episode_id'])

        # Adding M2M table for field que_series on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_que_series')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('tvseries', models.ForeignKey(orm['Schemas.tvseries'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'tvseries_id'])

        # Adding M2M table for field que_movies on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_que_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('movie', models.ForeignKey(orm['Schemas.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'movie_id'])

        # Adding M2M table for field que_episodes on 'UserProfile'
        m2m_table_name = db.shorten_name('profiles_userprofile_que_episodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['profiles.userprofile'], null=False)),
            ('episode', models.ForeignKey(orm['Schemas.episode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'episode_id'])

        # Adding model 'UserReviewedSeries'
        db.create_table('profiles_userreviewedseries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('review', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Review'], unique=True)),
            (
                'title',
                self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.TVSeries'], unique=True)),
        ))
        db.send_create_signal('profiles', ['UserReviewedSeries'])

        # Adding model 'UserReviewedMovie'
        db.create_table('profiles_userreviewedmovie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('review', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Review'], unique=True)),
            ('title', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Movie'], unique=True)),
        ))
        db.send_create_signal('profiles', ['UserReviewedMovie'])

        # Adding model 'UserReviewedEpisode'
        db.create_table('profiles_userreviewedepisode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('review', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Review'], unique=True)),
            ('title', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Episode'], unique=True)),
        ))
        db.send_create_signal('profiles', ['UserReviewedEpisode'])

        # Adding model 'UserRatedSeries'
        db.create_table('profiles_userratedseries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('rating',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.AggregateRating'], unique=True)),
            (
                'title',
                self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.TVSeries'], unique=True)),
        ))
        db.send_create_signal('profiles', ['UserRatedSeries'])

        # Adding model 'UserRatedMovie'
        db.create_table('profiles_userratedmovie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('rating',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.AggregateRating'], unique=True)),
            ('title', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Movie'], unique=True)),
        ))
        db.send_create_signal('profiles', ['UserRatedMovie'])

        # Adding model 'UserRatedEpisode'
        db.create_table('profiles_userratedepisode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('rating',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.AggregateRating'], unique=True)),
            ('title', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Schemas.Episode'], unique=True)),
        ))
        db.send_create_signal('profiles', ['UserRatedEpisode'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('profiles_userprofile')

        # Removing M2M table for field liked_series on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_liked_series'))

        # Removing M2M table for field liked_movies on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_liked_movies'))

        # Removing M2M table for field liked_episodes on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_liked_episodes'))

        # Removing M2M table for field watched_series on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_watched_series'))

        # Removing M2M table for field watched_movies on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_watched_movies'))

        # Removing M2M table for field watched_episodes on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_watched_episodes'))

        # Removing M2M table for field rated_series on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_rated_series'))

        # Removing M2M table for field rated_movies on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_rated_movies'))

        # Removing M2M table for field rated_episodes on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_rated_episodes'))

        # Removing M2M table for field reviewed_series on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_reviewed_series'))

        # Removing M2M table for field reviewed_movies on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_reviewed_movies'))

        # Removing M2M table for field reviewed_episodes on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_reviewed_episodes'))

        # Removing M2M table for field que_series on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_que_series'))

        # Removing M2M table for field que_movies on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_que_movies'))

        # Removing M2M table for field que_episodes on 'UserProfile'
        db.delete_table(db.shorten_name('profiles_userprofile_que_episodes'))

        # Deleting model 'UserReviewedSeries'
        db.delete_table('profiles_userreviewedseries')

        # Deleting model 'UserReviewedMovie'
        db.delete_table('profiles_userreviewedmovie')

        # Deleting model 'UserReviewedEpisode'
        db.delete_table('profiles_userreviewedepisode')

        # Deleting model 'UserRatedSeries'
        db.delete_table('profiles_userratedseries')

        # Deleting model 'UserRatedMovie'
        db.delete_table('profiles_userratedmovie')

        # Deleting model 'UserRatedEpisode'
        db.delete_table('profiles_userratedepisode')


    models = {
        'Schemas.aggregaterating': {
            'Meta': {'object_name': 'AggregateRating'},
            'bestRating': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemReviewed': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'ratingCount': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'ratingValue': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'reviewCount': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'worstRating': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'Schemas.country': {
            'Meta': {'object_name': 'Country'},
            'globalLocationNumber': (
                'django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'logo': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"})
        },
        'Schemas.episode': {
            'Meta': {'object_name': 'Episode'},
            'episodeNumber': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'new_episode': ('django.db.models.fields.related.OneToOneField', [],
                            {'to': "orm['series.NewEpisode']", 'blank': 'True', 'null': 'True', 'unique': 'True',
                             'default': 'None'}),
            'partOfSeason': ('django.db.models.fields.related.ForeignKey', [],
                             {'to': "orm['Schemas.Season']", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'partOfSeries': ('django.db.models.fields.related.ForeignKey', [],
                             {'to': "orm['Schemas.TVSeries']", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'subtitle_rating': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'views': ('django.db.models.fields.related.ManyToManyField', [],
                      {'symmetrical': 'False', 'to': "orm['Schemas.View']", 'null': 'True', 'blank': 'True',
                       'default': 'None'})
        },
        'Schemas.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'Schemas.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'Schemas.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.SlugField', [],
                    {'blank': 'True', 'null': 'True', 'max_length': '50', 'default': 'None'})
        },
        'Schemas.movie': {
            'Meta': {'_ormbases': ['Schemas.TVBase'], 'object_name': 'Movie'},
            'imdb': ('django.db.models.fields.related.OneToOneField', [],
                     {'to': "orm['imdb.Movies']", 'blank': 'True', 'null': 'True', 'unique': 'True',
                      'default': 'None'}),
            'is_czech': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'new_movie': ('django.db.models.fields.related.OneToOneField', [],
                          {'to': "orm['series.NewMovie']", 'blank': 'True', 'null': 'True', 'unique': 'True',
                           'default': 'None'}),
            'tvbase_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'to': "orm['Schemas.TVBase']", 'primary_key': 'True', 'unique': 'True'})
        },
        'Schemas.musicgroup': {
            'Meta': {'db_table': "'music_group_schema'", 'object_name': 'MusicGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"})
        },
        'Schemas.organization': {
            'Meta': {'object_name': 'Organization'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'blank': 'True', 'null': 'True', 'max_length': '200', 'default': 'None'})
        },
        'Schemas.person': {
            'Meta': {'object_name': 'Person'},
            'birthDate': (
                'django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'deathDate': (
                'django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'duns': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'gender': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [],
                            {'to': "orm['Schemas.Country']", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'blank': 'True', 'null': 'True', 'max_length': '200', 'default': 'None'})
        },
        'Schemas.rating': {
            'Meta': {'object_name': 'Rating'},
            'bestRating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratingValue': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'worstRating': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'Schemas.review': {
            'Meta': {'object_name': 'Review'},
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': "orm['Schemas.AggregateRating']", 'null': 'True',
                                  'blank': 'True', 'default': 'None'}),
            'dateCreated': (
                'django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'date_reviewed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'CS cz'"}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'itemReviewed': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [],
                         {'symmetrical': 'False', 'to': "orm['Schemas.Keyword']", 'null': 'True', 'blank': 'True',
                          'default': 'None'}),
            'reviewBody': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'reviewRating': ('django.db.models.fields.related.OneToOneField', [],
                             {'to': "orm['Schemas.Rating']", 'blank': 'True', 'null': 'True', 'unique': 'True',
                              'default': 'None'})
        },
        'Schemas.season': {
            'Meta': {'object_name': 'Season'},
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'numberOfEpisodes': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'partOfSeries': ('django.db.models.fields.related.ForeignKey', [],
                             {'to': "orm['Schemas.TVSeries']", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'startDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'Schemas.tvbase': {
            'Meta': {'object_name': 'TVBase'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': "orm['Schemas.Person']", 'related_name': "'actors'",
                        'null': 'True', 'blank': 'True', 'default': 'None'}),
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': "orm['Schemas.AggregateRating']",
                                  'related_name': "'ratings'", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'alternateName': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'cinematographers': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': "orm['Schemas.Person']",
                                  'related_name': "'cinematographers'", 'null': 'True', 'blank': 'True',
                                  'default': 'None'}),
            'datePublished': (
                'django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'director': ('django.db.models.fields.related.ManyToManyField', [],
                         {'symmetrical': 'False', 'to': "orm['Schemas.Person']", 'related_name': "'directors'",
                          'null': 'True', 'blank': 'True', 'default': 'None'}),
            'distributors': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.Organization']",
                              'related_name': "'distributors'", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [],
                      {'symmetrical': 'False', 'to': "orm['Schemas.Genre']", 'null': 'True', 'blank': 'True',
                       'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'images': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': "orm['Schemas.Image']", 'related_name': "'image_group'",
                        'null': 'True', 'blank': 'True', 'default': 'None'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "'Cs cz'"}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'isFamilyFriendly': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [],
                         {'symmetrical': 'False', 'to': "orm['Schemas.Keyword']", 'null': 'True', 'blank': 'True',
                          'default': 'None'}),
            'musicBy': ('django.db.models.fields.related.ManyToManyField', [],
                        {'symmetrical': 'False', 'to': "orm['Schemas.Person']", 'related_name': "'musician'",
                         'null': 'True', 'blank': 'True', 'default': 'None'}),
            'musicByGroup': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.MusicGroup']",
                              'related_name': "'music_group'", 'null': 'True', 'blank': 'True', 'default': 'None'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'numberOfEpisodes': (
                'django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'producer': ('django.db.models.fields.related.ManyToManyField', [],
                         {'symmetrical': 'False', 'to': "orm['Schemas.Person']", 'related_name': "'producer'",
                          'null': 'True', 'blank': 'True', 'default': 'None'}),
            'production_companies': ('django.db.models.fields.related.ManyToManyField', [],
                                     {'symmetrical': 'False', 'to': "orm['Schemas.Organization']",
                                      'related_name': "'production_companies'", 'null': 'True', 'blank': 'True',
                                      'default': 'None'}),
            'review': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': "orm['Schemas.Review']", 'null': 'True', 'blank': 'True',
                        'default': 'None'}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'blank': 'True', 'null': 'True', 'max_length': '200', 'default': 'None'}),
            'videoObject': ('django.db.models.fields.related.ManyToManyField', [],
                            {'symmetrical': 'False', 'to': "orm['Schemas.VideoObject']", 'null': 'True',
                             'blank': 'True', 'default': 'None'}),
            'views': ('django.db.models.fields.related.ManyToManyField', [],
                      {'symmetrical': 'False', 'to': "orm['Schemas.View']", 'null': 'True', 'blank': 'True',
                       'default': 'None'}),
            'writers': ('django.db.models.fields.related.ManyToManyField', [],
                        {'symmetrical': 'False', 'to': "orm['Schemas.Person']", 'related_name': "'writers'",
                         'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'Schemas.tvseries': {
            'Meta': {'_ormbases': ['Schemas.TVBase'], 'object_name': 'TVSeries'},
            'imdb': ('django.db.models.fields.related.OneToOneField', [],
                     {'to': "orm['imdb.Movies']", 'blank': 'True', 'null': 'True', 'unique': 'True',
                      'default': 'None'}),
            'new_show': ('django.db.models.fields.related.OneToOneField', [],
                         {'to': "orm['series.NewShow']", 'blank': 'True', 'null': 'True', 'unique': 'True',
                          'default': 'None'}),
            'tvbase_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'to': "orm['Schemas.TVBase']", 'primary_key': 'True', 'unique': 'True'})
        },
        'Schemas.videoobject': {
            'Meta': {'object_name': 'VideoObject'},
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': "orm['Schemas.AggregateRating']", 'null': 'True',
                                  'blank': 'True', 'default': 'None'}),
            'embedUrl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'encodingFormat': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'CS cz'"}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'productionCompany': ('django.db.models.fields.related.ManyToManyField', [],
                                  {'symmetrical': 'False', 'to': "orm['Schemas.Organization']", 'null': 'True',
                                   'blank': 'True', 'default': 'None'}),
            'uploadDate': (
                'django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'videoFrameSize': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"}),
            'videoQuality': (
                'django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'default': "''"})
        },
        'Schemas.view': {
            'Meta': {'object_name': 'View'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'view_count': ('django.db.models.fields.BigIntegerField', [], {}),
            'view_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                            {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission',
                     'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
                'django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'",
                        'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'",
                                  'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'imdb.movies': {
            'Meta': {'db_table': "'movies'", 'object_name': 'Movies'},
            'imdbid': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10'}),
            'movieid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'year': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'})
        },
        'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'active_int': ('django.db.models.fields.BigIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked_episodes': ('django.db.models.fields.related.ManyToManyField', [],
                               {'symmetrical': 'False', 'to': "orm['Schemas.Episode']",
                                'related_name': "'liked_episodes'", 'null': 'True', 'blank': 'True',
                                'default': 'None'}),
            'liked_movies': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.Movie']", 'related_name': "'liked_movies'",
                              'null': 'True', 'blank': 'True', 'default': 'None'}),
            'liked_series': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.TVSeries']", 'related_name': "'liked_series'",
                              'null': 'True', 'blank': 'True', 'default': 'None'}),
            'picture': ('django.db.models.fields.files.ImageField', [],
                        {'blank': 'True', 'null': 'True', 'max_length': '100', 'default': 'None'}),
            'que_episodes': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.Episode']", 'related_name': "'que_episodes'",
                              'null': 'True', 'blank': 'True', 'default': 'None'}),
            'que_movies': ('django.db.models.fields.related.ManyToManyField', [],
                           {'symmetrical': 'False', 'to': "orm['Schemas.Movie']", 'related_name': "'que_movies'",
                            'null': 'True', 'blank': 'True', 'default': 'None'}),
            'que_series': ('django.db.models.fields.related.ManyToManyField', [],
                           {'symmetrical': 'False', 'to': "orm['Schemas.TVSeries']", 'related_name': "'que_series'",
                            'null': 'True', 'blank': 'True', 'default': 'None'}),
            'rated_episodes': ('django.db.models.fields.related.ManyToManyField', [],
                               {'symmetrical': 'False', 'to': "orm['Schemas.Episode']",
                                'related_name': "'rated_episodes'", 'null': 'True', 'blank': 'True',
                                'default': 'None'}),
            'rated_movies': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.Movie']", 'related_name': "'rated_movies'",
                              'null': 'True', 'blank': 'True', 'default': 'None'}),
            'rated_series': ('django.db.models.fields.related.ManyToManyField', [],
                             {'symmetrical': 'False', 'to': "orm['Schemas.TVSeries']", 'related_name': "'rated_series'",
                              'null': 'True', 'blank': 'True', 'default': 'None'}),
            'reviewed_episodes': ('django.db.models.fields.related.ManyToManyField', [],
                                  {'symmetrical': 'False', 'to': "orm['Schemas.Episode']",
                                   'related_name': "'reviewed_episodes'", 'null': 'True', 'blank': 'True',
                                   'default': 'None'}),
            'reviewed_movies': ('django.db.models.fields.related.ManyToManyField', [],
                                {'symmetrical': 'False', 'to': "orm['Schemas.Movie']",
                                 'related_name': "'reviewed_movies'", 'null': 'True', 'blank': 'True',
                                 'default': 'None'}),
            'reviewed_series': ('django.db.models.fields.related.ManyToManyField', [],
                                {'symmetrical': 'False', 'to': "orm['Schemas.TVSeries']",
                                 'related_name': "'reviewed_series'", 'null': 'True', 'blank': 'True',
                                 'default': 'None'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'watched_episodes': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': "orm['Schemas.Episode']",
                                  'related_name': "'watched_episodes'", 'null': 'True', 'blank': 'True',
                                  'default': 'None'}),
            'watched_movies': ('django.db.models.fields.related.ManyToManyField', [],
                               {'symmetrical': 'False', 'to': "orm['Schemas.Movie']",
                                'related_name': "'watched_movies'", 'null': 'True', 'blank': 'True',
                                'default': 'None'}),
            'watched_series': ('django.db.models.fields.related.ManyToManyField', [],
                               {'symmetrical': 'False', 'to': "orm['Schemas.TVSeries']",
                                'related_name': "'watched_series'", 'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'profiles.userratedepisode': {
            'Meta': {'object_name': 'UserRatedEpisode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.related.OneToOneField', [],
                       {'to': "orm['Schemas.AggregateRating']", 'unique': 'True'}),
            'title': (
                'django.db.models.fields.related.OneToOneField', [],
                {'to': "orm['Schemas.Episode']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.userratedmovie': {
            'Meta': {'object_name': 'UserRatedMovie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.related.OneToOneField', [],
                       {'to': "orm['Schemas.AggregateRating']", 'unique': 'True'}),
            'title': (
                'django.db.models.fields.related.OneToOneField', [], {'to': "orm['Schemas.Movie']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.userratedseries': {
            'Meta': {'object_name': 'UserRatedSeries'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.related.OneToOneField', [],
                       {'to': "orm['Schemas.AggregateRating']", 'unique': 'True'}),
            'title': (
                'django.db.models.fields.related.OneToOneField', [],
                {'to': "orm['Schemas.TVSeries']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.userreviewedepisode': {
            'Meta': {'object_name': 'UserReviewedEpisode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': (
                'django.db.models.fields.related.OneToOneField', [], {'to': "orm['Schemas.Review']", 'unique': 'True'}),
            'title': (
                'django.db.models.fields.related.OneToOneField', [],
                {'to': "orm['Schemas.Episode']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.userreviewedmovie': {
            'Meta': {'object_name': 'UserReviewedMovie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': (
                'django.db.models.fields.related.OneToOneField', [], {'to': "orm['Schemas.Review']", 'unique': 'True'}),
            'title': (
                'django.db.models.fields.related.OneToOneField', [], {'to': "orm['Schemas.Movie']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'profiles.userreviewedseries': {
            'Meta': {'object_name': 'UserReviewedSeries'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': (
                'django.db.models.fields.related.OneToOneField', [], {'to': "orm['Schemas.Review']", 'unique': 'True'}),
            'title': (
                'django.db.models.fields.related.OneToOneField', [],
                {'to': "orm['Schemas.TVSeries']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'series.newepisode': {
            'Meta': {'db_table': "'new_episode'", 'object_name': 'NewEpisode'},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'db_column': "'link'"}),
            'show_title': ('django.db.models.fields.TextField', [], {'db_column': "'show_title'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        },
        'series.newmovie': {
            'Meta': {'db_table': "'new_movie'", 'object_name': 'NewMovie'},
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
            'Meta': {'db_table': "'new_show'", 'object_name': 'NewShow'},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'db_column': "'image'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        }
    }

    complete_apps = ['profiles']