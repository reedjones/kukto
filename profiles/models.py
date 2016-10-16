# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from django.contrib.auth.models import User
from django.db import models

from kukto.Schemas.models import TVSeries, Movie, Episode, AggregateRating, Review


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    active_int = models.BigIntegerField(default=1)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True, default=None)
    liked_series = models.ManyToManyField(TVSeries, null=True, default=None, blank=True, related_name='liked_series',db_table='profiles_userprofile_liked_series')
    liked_movies = models.ManyToManyField(Movie, null=True, default=None, blank=True, related_name='liked_movies',db_table='profiles_userprofile_liked_movies')
    liked_episodes = models.ManyToManyField(Episode, null=True, default=None, blank=True, related_name='liked_episodes',db_table='profiles_userprofile_liked_episodes')

    watched_series = models.ManyToManyField(TVSeries, null=True, default=None, blank=True,
                                            related_name='watched_series',db_table='profiles_userprofile_watched_series')

    watched_movies = models.ManyToManyField(Movie, null=True, default=None, blank=True, related_name='watched_movies',db_table='profiles_userprofile_watched_movies')

    watched_episodes = models.ManyToManyField(Episode, null=True, default=None, blank=True,
                                              related_name='watched_episodes',db_table='profiles_userprofile_watched_episodes')

    rated_series = models.ManyToManyField(TVSeries, null=True, default=None, blank=True, related_name='rated_series',db_table='profiles_userprofile_rated_series')

    rated_movies = models.ManyToManyField(Movie, null=True, default=None, blank=True, related_name='rated_movies',db_table='profiles_userprofile_rated_movies')

    rated_episodes = models.ManyToManyField(Episode, null=True, default=None, blank=True, related_name='rated_episodes',db_table='profiles_userprofile_rated_episodes')

    reviewed_series = models.ManyToManyField(TVSeries, null=True, default=None, blank=True,
                                             related_name='reviewed_series',db_table='profiles_userprofile_reviewed_series')

    reviewed_movies = models.ManyToManyField(Movie, null=True, default=None, blank=True, related_name='reviewed_movies',db_table='profiles_userprofile_reviewed_movies')

    reviewed_episodes = models.ManyToManyField(Episode, null=True, default=None, blank=True,
                                               related_name='reviewed_episodes',db_table='profiles_userprofile_reviewed_episodes')

    que_series = models.ManyToManyField(TVSeries, null=True, default=None, blank=True, related_name='que_series',db_table='profiles_userprofile_que_series')
    que_movies = models.ManyToManyField(Movie, null=True, default=None, blank=True, related_name='que_movies',db_table='profiles_userprofile_que_movies')
    que_episodes = models.ManyToManyField(Episode, null=True, default=None, blank=True, related_name='que_episodes',db_table='profiles_userprofile_que_episodes')

    class Meta(object):
        db_table = 'profiles_userprofile'


class UserReviewedSeries(models.Model):
    user = models.OneToOneField(User)
    review = models.OneToOneField(Review)
    title = models.OneToOneField(TVSeries)
    class Meta(object):
        db_table='profiles_userreviewedseries'


class UserReviewedMovie(models.Model):
    user = models.OneToOneField(User)
    review = models.OneToOneField(Review)
    title = models.OneToOneField(Movie)
    class Meta(object):
        db_table='profiles_userreviewedmovie'


class UserReviewedEpisode(models.Model):
    user = models.OneToOneField(User)
    review = models.OneToOneField(Review)
    title = models.OneToOneField(Episode)
    class Meta(object):
        db_table='profiles_userreviewedepisode'


class UserRatedSeries(models.Model):
    user = models.OneToOneField(User)
    rating = models.OneToOneField(AggregateRating)
    title = models.OneToOneField(TVSeries)
    class Meta(object):
        db_table='profiles_userratedseries'


class UserRatedMovie(models.Model):
    user = models.OneToOneField(User)
    rating = models.OneToOneField(AggregateRating)
    title = models.OneToOneField(Movie)
    class Meta(object):
        db_table='profiles_userratedmovie'


class UserRatedEpisode(models.Model):
    user = models.OneToOneField(User)
    rating = models.OneToOneField(AggregateRating)
    title = models.OneToOneField(Episode)

    class Meta(object):
        db_table='profiles_userratedepisode'


