# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'MusicGroup'
        db.create_table('music_group_schema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal('Schemas', ['MusicGroup'])

        # Adding model 'Keyword'
        db.create_table('Schemas_keyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.SlugField')(default=None, blank=True, max_length=50, null=True)),
        ))
        db.send_create_signal('Schemas', ['Keyword'])

        # Adding model 'AggregateRating'
        db.create_table('Schemas_aggregaterating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemReviewed', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('ratingCount', self.gf('django.db.models.fields.BigIntegerField')(default=None, blank=True, null=True)),
            ('reviewCount', self.gf('django.db.models.fields.BigIntegerField')(default=None, blank=True, null=True)),
            ('bestRating', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
            ('worstRating', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
            ('ratingValue', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['AggregateRating'])

        # Adding model 'Rating'
        db.create_table('Schemas_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bestRating', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('worstRating', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('ratingValue', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['Rating'])

        # Adding model 'Organization'
        db.create_table('Schemas_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            (
                'sameAs',
                self.gf('django.db.models.fields.URLField')(default=None, blank=True, max_length=200, null=True)),
            ('image', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('Schemas', ['Organization'])

        # Adding model 'Country'
        db.create_table('Schemas_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('globalLocationNumber',
             self.gf('django.db.models.fields.BigIntegerField')(default=None, blank=True, null=True)),
            ('image', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('logo', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('Schemas', ['Country'])

        # Adding model 'Person'
        db.create_table('Schemas_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('birthDate', self.gf('django.db.models.fields.DateField')(default=None, blank=True, null=True)),
            ('deathDate', self.gf('django.db.models.fields.DateField')(default=None, blank=True, null=True)),
            ('duns', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(default=None, blank=True, null=True,
                                                                                  to=orm['Schemas.Country'])),
            (
                'sameAs',
                self.gf('django.db.models.fields.URLField')(default=None, blank=True, max_length=200, null=True)),
            ('images', self.gf('django.db.models.fields.TextField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['Person'])

        # Adding model 'Image'
        db.create_table('Schemas_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('src', self.gf('django.db.models.fields.TextField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['Image'])

        # Adding model 'Actor'
        db.create_table('Schemas_actor', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True,
                                                                                    to=orm['Schemas.Person'])),
            ('person_id', self.gf('django.db.models.fields.BigIntegerField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['Actor'])

        # Adding model 'Review'
        db.create_table('Schemas_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemReviewed', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('reviewBody', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('reviewRating',
             self.gf('django.db.models.fields.related.OneToOneField')(default=None, blank=True, null=True, unique=True,
                                                                      to=orm['Schemas.Rating'])),
            ('dateCreated', self.gf('django.db.models.fields.DateField')(default=None, blank=True, null=True)),
            ('date_reviewed', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('inLanguage', self.gf('django.db.models.fields.CharField')(default='CS cz', max_length=100)),
            ('interactionCount', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal('Schemas', ['Review'])

        # Adding M2M table for field aggregate_rating on 'Review'
        m2m_table_name = db.shorten_name('Schemas_review_aggregate_rating')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('review', models.ForeignKey(orm['Schemas.review'], null=False)),
            ('aggregaterating', models.ForeignKey(orm['Schemas.aggregaterating'], null=False))
        ))
        db.create_unique(m2m_table_name, ['review_id', 'aggregaterating_id'])

        # Adding M2M table for field keywords on 'Review'
        m2m_table_name = db.shorten_name('Schemas_review_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('review', models.ForeignKey(orm['Schemas.review'], null=False)),
            ('keyword', models.ForeignKey(orm['Schemas.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['review_id', 'keyword_id'])

        # Adding model 'VideoObject'
        db.create_table('Schemas_videoobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('videoFrameSize', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('videoQuality', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('encodingFormat', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('interactionCount', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('uploadDate', self.gf('django.db.models.fields.DateTimeField')(default=None, blank=True, null=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('inLanguage', self.gf('django.db.models.fields.CharField')(default='CS cz', max_length=100)),
            ('embedUrl', self.gf('django.db.models.fields.TextField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['VideoObject'])

        # Adding M2M table for field productionCompany on 'VideoObject'
        m2m_table_name = db.shorten_name('Schemas_videoobject_productionCompany')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videoobject', models.ForeignKey(orm['Schemas.videoobject'], null=False)),
            ('organization', models.ForeignKey(orm['Schemas.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['videoobject_id', 'organization_id'])

        # Adding M2M table for field aggregate_rating on 'VideoObject'
        m2m_table_name = db.shorten_name('Schemas_videoobject_aggregate_rating')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videoobject', models.ForeignKey(orm['Schemas.videoobject'], null=False)),
            ('aggregaterating', models.ForeignKey(orm['Schemas.aggregaterating'], null=False))
        ))
        db.create_unique(m2m_table_name, ['videoobject_id', 'aggregaterating_id'])

        # Adding model 'Genre'
        db.create_table('Schemas_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('Schemas', ['Genre'])

        # Adding model 'View'
        db.create_table('Schemas_view', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('view_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('view_count', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('Schemas', ['View'])

        # Adding model 'TVBase'
        db.create_table('Schemas_tvbase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numberOfEpisodes', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
            ('datePublished', self.gf('django.db.models.fields.DateTimeField')(default=None, blank=True, null=True)),
            ('inLanguage', self.gf('django.db.models.fields.CharField')(default='Cs cz', max_length=200)),
            ('interactionCount', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('likes', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('isFamilyFriendly', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('image', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('alternateName', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            (
                'sameAs',
                self.gf('django.db.models.fields.URLField')(default=None, blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('Schemas', ['TVBase'])

        # Adding M2M table for field views on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_views')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('view', models.ForeignKey(orm['Schemas.view'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'view_id'])

        # Adding M2M table for field actors on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_actors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('person', models.ForeignKey(orm['Schemas.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'person_id'])

        # Adding M2M table for field director on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_director')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('person', models.ForeignKey(orm['Schemas.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'person_id'])

        # Adding M2M table for field writers on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_writers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('person', models.ForeignKey(orm['Schemas.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'person_id'])

        # Adding M2M table for field cinematographers on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_cinematographers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('person', models.ForeignKey(orm['Schemas.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'person_id'])

        # Adding M2M table for field distributors on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_distributors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('organization', models.ForeignKey(orm['Schemas.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'organization_id'])

        # Adding M2M table for field musicBy on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_musicBy')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('person', models.ForeignKey(orm['Schemas.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'person_id'])

        # Adding M2M table for field musicByGroup on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_musicByGroup')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('musicgroup', models.ForeignKey(orm['Schemas.musicgroup'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'musicgroup_id'])

        # Adding M2M table for field producer on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_producer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('person', models.ForeignKey(orm['Schemas.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'person_id'])

        # Adding M2M table for field genre on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('genre', models.ForeignKey(orm['Schemas.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'genre_id'])

        # Adding M2M table for field keywords on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('keyword', models.ForeignKey(orm['Schemas.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'keyword_id'])

        # Adding M2M table for field review on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_review')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('review', models.ForeignKey(orm['Schemas.review'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'review_id'])

        # Adding M2M table for field images on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('image', models.ForeignKey(orm['Schemas.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'image_id'])

        # Adding M2M table for field videoObject on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_videoObject')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('videoobject', models.ForeignKey(orm['Schemas.videoobject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'videoobject_id'])

        # Adding M2M table for field aggregate_rating on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_aggregate_rating')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('aggregaterating', models.ForeignKey(orm['Schemas.aggregaterating'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'aggregaterating_id'])

        # Adding M2M table for field production_companies on 'TVBase'
        m2m_table_name = db.shorten_name('Schemas_tvbase_production_companies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tvbase', models.ForeignKey(orm['Schemas.tvbase'], null=False)),
            ('organization', models.ForeignKey(orm['Schemas.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tvbase_id', 'organization_id'])

        # Adding model 'TVSeries'
        db.create_table('Schemas_tvseries', (
            ('tvbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True,
                                                                                    to=orm['Schemas.TVBase'])),
            ('new_show',
             self.gf('django.db.models.fields.related.OneToOneField')(default=None, blank=True, null=True, unique=True,
                                                                      to=orm['series.NewShow'])),
            ('imdb',
             self.gf('django.db.models.fields.related.OneToOneField')(default=None, blank=True, null=True, unique=True,
                                                                      to=orm['imdb.Movies'])),
        ))
        db.send_create_signal('Schemas', ['TVSeries'])

        # Adding model 'Movie'
        db.create_table('Schemas_movie', (
            ('tvbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True,
                                                                                    to=orm['Schemas.TVBase'])),
            ('is_czech', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('new_movie',
             self.gf('django.db.models.fields.related.OneToOneField')(default=None, blank=True, null=True, unique=True,
                                                                      to=orm['series.NewMovie'])),
            ('imdb',
             self.gf('django.db.models.fields.related.OneToOneField')(default=None, blank=True, null=True, unique=True,
                                                                      to=orm['imdb.Movies'])),
        ))
        db.send_create_signal('Schemas', ['Movie'])

        # Adding model 'Season'
        db.create_table('Schemas_season', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numberOfEpisodes', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
            ('partOfSeries', self.gf('django.db.models.fields.related.ForeignKey')(default=None, blank=True, null=True,
                                                                                   to=orm['Schemas.TVSeries'])),
            ('startDate', self.gf('django.db.models.fields.DateField')(default=None, blank=True, null=True)),
            ('endDate', self.gf('django.db.models.fields.DateField')(default=None, blank=True, null=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['Season'])

        # Adding model 'Episode'
        db.create_table('Schemas_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episodeNumber', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
            ('partOfSeason', self.gf('django.db.models.fields.related.ForeignKey')(default=None, blank=True, null=True,
                                                                                   to=orm['Schemas.Season'])),
            ('partOfSeries', self.gf('django.db.models.fields.related.ForeignKey')(default=None, blank=True, null=True,
                                                                                   to=orm['Schemas.TVSeries'])),
            ('new_episode',
             self.gf('django.db.models.fields.related.OneToOneField')(default=None, blank=True, null=True, unique=True,
                                                                      to=orm['series.NewEpisode'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('interactionCount', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('subtitle_rating', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('Schemas', ['Episode'])

        # Adding M2M table for field views on 'Episode'
        m2m_table_name = db.shorten_name('Schemas_episode_views')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('episode', models.ForeignKey(orm['Schemas.episode'], null=False)),
            ('view', models.ForeignKey(orm['Schemas.view'], null=False))
        ))
        db.create_unique(m2m_table_name, ['episode_id', 'view_id'])


    def backwards(self, orm):
        # Deleting model 'MusicGroup'
        db.delete_table('music_group_schema')

        # Deleting model 'Keyword'
        db.delete_table('Schemas_keyword')

        # Deleting model 'AggregateRating'
        db.delete_table('Schemas_aggregaterating')

        # Deleting model 'Rating'
        db.delete_table('Schemas_rating')

        # Deleting model 'Organization'
        db.delete_table('Schemas_organization')

        # Deleting model 'Country'
        db.delete_table('Schemas_country')

        # Deleting model 'Person'
        db.delete_table('Schemas_person')

        # Deleting model 'Image'
        db.delete_table('Schemas_image')

        # Deleting model 'Actor'
        db.delete_table('Schemas_actor')

        # Deleting model 'Review'
        db.delete_table('Schemas_review')

        # Removing M2M table for field aggregate_rating on 'Review'
        db.delete_table(db.shorten_name('Schemas_review_aggregate_rating'))

        # Removing M2M table for field keywords on 'Review'
        db.delete_table(db.shorten_name('Schemas_review_keywords'))

        # Deleting model 'VideoObject'
        db.delete_table('Schemas_videoobject')

        # Removing M2M table for field productionCompany on 'VideoObject'
        db.delete_table(db.shorten_name('Schemas_videoobject_productionCompany'))

        # Removing M2M table for field aggregate_rating on 'VideoObject'
        db.delete_table(db.shorten_name('Schemas_videoobject_aggregate_rating'))

        # Deleting model 'Genre'
        db.delete_table('Schemas_genre')

        # Deleting model 'View'
        db.delete_table('Schemas_view')

        # Deleting model 'TVBase'
        db.delete_table('Schemas_tvbase')

        # Removing M2M table for field views on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_views'))

        # Removing M2M table for field actors on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_actors'))

        # Removing M2M table for field director on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_director'))

        # Removing M2M table for field writers on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_writers'))

        # Removing M2M table for field cinematographers on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_cinematographers'))

        # Removing M2M table for field distributors on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_distributors'))

        # Removing M2M table for field musicBy on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_musicBy'))

        # Removing M2M table for field musicByGroup on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_musicByGroup'))

        # Removing M2M table for field producer on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_producer'))

        # Removing M2M table for field genre on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_genre'))

        # Removing M2M table for field keywords on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_keywords'))

        # Removing M2M table for field review on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_review'))

        # Removing M2M table for field images on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_images'))

        # Removing M2M table for field videoObject on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_videoObject'))

        # Removing M2M table for field aggregate_rating on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_aggregate_rating'))

        # Removing M2M table for field production_companies on 'TVBase'
        db.delete_table(db.shorten_name('Schemas_tvbase_production_companies'))

        # Deleting model 'TVSeries'
        db.delete_table('Schemas_tvseries')

        # Deleting model 'Movie'
        db.delete_table('Schemas_movie')

        # Deleting model 'Season'
        db.delete_table('Schemas_season')

        # Deleting model 'Episode'
        db.delete_table('Schemas_episode')

        # Removing M2M table for field views on 'Episode'
        db.delete_table(db.shorten_name('Schemas_episode_views'))


    models = {
        'Schemas.actor': {
            'Meta': {'object_name': 'Actor', '_ormbases': ['Schemas.Person']},
            'person_id': (
                'django.db.models.fields.BigIntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'primary_key': 'True', 'unique': 'True', 'to': "orm['Schemas.Person']"})
        },
        'Schemas.aggregaterating': {
            'Meta': {'object_name': 'AggregateRating'},
            'bestRating': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemReviewed': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'ratingCount': (
                'django.db.models.fields.BigIntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'ratingValue': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'reviewCount': (
                'django.db.models.fields.BigIntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'worstRating': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'})
        },
        'Schemas.country': {
            'Meta': {'object_name': 'Country'},
            'globalLocationNumber': (
                'django.db.models.fields.BigIntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'logo': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'Schemas.episode': {
            'Meta': {'object_name': 'Episode'},
            'episodeNumber': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'new_episode': ('django.db.models.fields.related.OneToOneField', [],
                            {'default': 'None', 'blank': 'True', 'null': 'True', 'unique': 'True',
                             'to': "orm['series.NewEpisode']"}),
            'partOfSeason': ('django.db.models.fields.related.ForeignKey', [],
                             {'default': 'None', 'blank': 'True', 'null': 'True', 'to': "orm['Schemas.Season']"}),
            'partOfSeries': ('django.db.models.fields.related.ForeignKey', [],
                             {'default': 'None', 'blank': 'True', 'null': 'True', 'to': "orm['Schemas.TVSeries']"}),
            'subtitle_rating': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'views': ('django.db.models.fields.related.ManyToManyField', [],
                      {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                       'to': "orm['Schemas.View']"})
        },
        'Schemas.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'Schemas.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True', 'null': 'True'})
        },
        'Schemas.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.SlugField', [],
                    {'default': 'None', 'blank': 'True', 'max_length': '50', 'null': 'True'})
        },
        'Schemas.movie': {
            'Meta': {'object_name': 'Movie', '_ormbases': ['Schemas.TVBase']},
            'imdb': ('django.db.models.fields.related.OneToOneField', [],
                     {'default': 'None', 'blank': 'True', 'null': 'True', 'unique': 'True',
                      'to': "orm['imdb.Movies']"}),
            'is_czech': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'new_movie': ('django.db.models.fields.related.OneToOneField', [],
                          {'default': 'None', 'blank': 'True', 'null': 'True', 'unique': 'True',
                           'to': "orm['series.NewMovie']"}),
            'tvbase_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'primary_key': 'True', 'unique': 'True', 'to': "orm['Schemas.TVBase']"})
        },
        'Schemas.musicgroup': {
            'Meta': {'db_table': "'music_group_schema'", 'object_name': 'MusicGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'Schemas.organization': {
            'Meta': {'object_name': 'Organization'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'default': 'None', 'blank': 'True', 'max_length': '200', 'null': 'True'})
        },
        'Schemas.person': {
            'Meta': {'object_name': 'Person'},
            'birthDate': (
                'django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'deathDate': (
                'django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'duns': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'gender': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [],
                            {'default': 'None', 'blank': 'True', 'null': 'True', 'to': "orm['Schemas.Country']"}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'default': 'None', 'blank': 'True', 'max_length': '200', 'null': 'True'})
        },
        'Schemas.rating': {
            'Meta': {'object_name': 'Rating'},
            'bestRating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratingValue': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'worstRating': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'Schemas.review': {
            'Meta': {'object_name': 'Review'},
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                                  'to': "orm['Schemas.AggregateRating']"}),
            'dateCreated': (
                'django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'date_reviewed': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'default': "'CS cz'", 'max_length': '100'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'itemReviewed': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [],
                         {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                          'to': "orm['Schemas.Keyword']"}),
            'reviewBody': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'reviewRating': ('django.db.models.fields.related.OneToOneField', [],
                             {'default': 'None', 'blank': 'True', 'null': 'True', 'unique': 'True',
                              'to': "orm['Schemas.Rating']"})
        },
        'Schemas.season': {
            'Meta': {'object_name': 'Season'},
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'numberOfEpisodes': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'partOfSeries': ('django.db.models.fields.related.ForeignKey', [],
                             {'default': 'None', 'blank': 'True', 'null': 'True', 'to': "orm['Schemas.TVSeries']"}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'})
        },
        'Schemas.tvbase': {
            'Meta': {'object_name': 'TVBase'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [],
                       {'related_name': "'actors'", 'null': 'True', 'symmetrical': 'False',
                        'to': "orm['Schemas.Person']", 'default': 'None', 'blank': 'True'}),
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'related_name': "'ratings'", 'null': 'True', 'symmetrical': 'False',
                                  'to': "orm['Schemas.AggregateRating']", 'default': 'None', 'blank': 'True'}),
            'alternateName': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'cinematographers': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'related_name': "'cinematographers'", 'null': 'True', 'symmetrical': 'False',
                                  'to': "orm['Schemas.Person']", 'default': 'None', 'blank': 'True'}),
            'datePublished': (
                'django.db.models.fields.DateTimeField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [],
                         {'related_name': "'directors'", 'null': 'True', 'symmetrical': 'False',
                          'to': "orm['Schemas.Person']", 'default': 'None', 'blank': 'True'}),
            'distributors': ('django.db.models.fields.related.ManyToManyField', [],
                             {'related_name': "'distributors'", 'null': 'True', 'symmetrical': 'False',
                              'to': "orm['Schemas.Organization']", 'default': 'None', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [],
                      {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                       'to': "orm['Schemas.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [],
                       {'related_name': "'image_group'", 'null': 'True', 'symmetrical': 'False',
                        'to': "orm['Schemas.Image']", 'default': 'None', 'blank': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'default': "'Cs cz'", 'max_length': '200'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'isFamilyFriendly': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [],
                         {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                          'to': "orm['Schemas.Keyword']"}),
            'likes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'musicBy': ('django.db.models.fields.related.ManyToManyField', [],
                        {'related_name': "'musician'", 'null': 'True', 'symmetrical': 'False',
                         'to': "orm['Schemas.Person']", 'default': 'None', 'blank': 'True'}),
            'musicByGroup': ('django.db.models.fields.related.ManyToManyField', [],
                             {'related_name': "'music_group'", 'null': 'True', 'symmetrical': 'False',
                              'to': "orm['Schemas.MusicGroup']", 'default': 'None', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'numberOfEpisodes': (
                'django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'producer': ('django.db.models.fields.related.ManyToManyField', [],
                         {'related_name': "'producer'", 'null': 'True', 'symmetrical': 'False',
                          'to': "orm['Schemas.Person']", 'default': 'None', 'blank': 'True'}),
            'production_companies': ('django.db.models.fields.related.ManyToManyField', [],
                                     {'related_name': "'production_companies'", 'null': 'True', 'symmetrical': 'False',
                                      'to': "orm['Schemas.Organization']", 'default': 'None', 'blank': 'True'}),
            'review': ('django.db.models.fields.related.ManyToManyField', [],
                       {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                        'to': "orm['Schemas.Review']"}),
            'sameAs': ('django.db.models.fields.URLField', [],
                       {'default': 'None', 'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'videoObject': ('django.db.models.fields.related.ManyToManyField', [],
                            {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                             'to': "orm['Schemas.VideoObject']"}),
            'views': ('django.db.models.fields.related.ManyToManyField', [],
                      {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                       'to': "orm['Schemas.View']"}),
            'writers': ('django.db.models.fields.related.ManyToManyField', [],
                        {'related_name': "'writers'", 'null': 'True', 'symmetrical': 'False',
                         'to': "orm['Schemas.Person']", 'default': 'None', 'blank': 'True'})
        },
        'Schemas.tvseries': {
            'Meta': {'object_name': 'TVSeries', '_ormbases': ['Schemas.TVBase']},
            'imdb': ('django.db.models.fields.related.OneToOneField', [],
                     {'default': 'None', 'blank': 'True', 'null': 'True', 'unique': 'True',
                      'to': "orm['imdb.Movies']"}),
            'new_show': ('django.db.models.fields.related.OneToOneField', [],
                         {'default': 'None', 'blank': 'True', 'null': 'True', 'unique': 'True',
                          'to': "orm['series.NewShow']"}),
            'tvbase_ptr': ('django.db.models.fields.related.OneToOneField', [],
                           {'primary_key': 'True', 'unique': 'True', 'to': "orm['Schemas.TVBase']"})
        },
        'Schemas.videoobject': {
            'Meta': {'object_name': 'VideoObject'},
            'aggregate_rating': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                                  'to': "orm['Schemas.AggregateRating']"}),
            'embedUrl': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'encodingFormat': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'default': "'CS cz'", 'max_length': '100'}),
            'interactionCount': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'productionCompany': ('django.db.models.fields.related.ManyToManyField', [],
                                  {'default': 'None', 'blank': 'True', 'symmetrical': 'False', 'null': 'True',
                                   'to': "orm['Schemas.Organization']"}),
            'uploadDate': (
                'django.db.models.fields.DateTimeField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'videoFrameSize': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'videoQuality': (
                'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'Schemas.view': {
            'Meta': {'object_name': 'View'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'view_count': ('django.db.models.fields.BigIntegerField', [], {}),
            'view_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'imdb.movies': {
            'Meta': {'db_table': "'movies'", 'object_name': 'Movies'},
            'imdbid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'movieid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'series.newepisode': {
            'Meta': {'db_table': "'new_episode'", 'object_name': 'NewEpisode'},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'db_column': "'link'"}),
            'show_title': ('django.db.models.fields.TextField', [], {'db_column': "'show_title'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        },
        'series.newmovie': {
            'Meta': {'db_table': "'new_movie'", 'object_name': 'NewMovie'},
            'date': (
                'django.db.models.fields.DateTimeField', [],
                {'db_column': "'date'", 'blank': 'True', 'auto_now': 'True'}),
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
                {'db_column': "'date'", 'blank': 'True', 'auto_now': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'id': ('django.db.models.fields.AutoField', [], {'db_column': "'id'", 'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'db_column': "'image'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "'title'"})
        }
    }

    complete_apps = ['Schemas']