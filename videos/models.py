# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from future.builtins import object
from future import standard_library

standard_library.install_hooks()
from kukto.Schemas.models import Keyword, AggregateRating,Episode,Movie,TVSeries, Review
from kukto.profiles.models import UserProfile


from django.db import models
from django.contrib import admin

#TODO Setting up the Badges, Alternate Links, and more

class alternateLink(models.Model):
    link = models.TextField()
    date = models.DateField(auto_now=True)
    uploaded_by = models.ForeignKey(UserProfile, related_name='added_links')
    requested_by = models.ManyToManyField(UserProfile, through='VideoRequest', related_name='requested_links')
    quality = models.IntegerField()
    is_flagged = models.NullBooleanField()

    class Meta(object):
        db_table='videos_alternatelink'

class VideoRequest(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(UserProfile)
    alternateLink = models.ForeignKey(alternateLink)

    class Meta(object):
        db_table='videos_videorequest'


class NewVideo(models.Model):
    is_subtitle = models.NullBooleanField()
    subtitle_rating = models.ForeignKey(AggregateRating,null=True,blank=True,default=None)
    alternate_links = models.ManyToManyField(alternateLink,default=None,blank=True,null=True,db_table='videos_newvideo_alternate_links')

    class Meta(object):
        db_table='videos_newvideo'

class EpisodeVideoObj(NewVideo):
    episode = models.ForeignKey(Episode)
    class Meta(object):
        db_table='videos_episodevideoobj'

class TVSeriesVideoObj(NewVideo):
    tv_series = models.ForeignKey(TVSeries)
    class Meta(object):
        db_table='videos_tvseriesvideoobj'

class MovieVideoObj(NewVideo):
    movie = models.ForeignKey(Movie)
    class Meta(object):
        db_table='videos_movievideoobj'

class BadgeGeneric(models.Model):
    user_has = models.ManyToManyField(UserProfile,through='GotAward')
    name = models.CharField(max_length=200)
    points_earned = models.IntegerField()
    points_needed = models.IntegerField()
    image = models.ImageField(upload_to='awards')
    max_num = models.IntegerField()
    class Meta(object):
        db_table='videos_badgegeneric'

class GotAward(models.Model):
    badge_generic = models.ForeignKey(BadgeGeneric)
    user = models.ForeignKey(UserProfile)
    date = models.DateField(auto_now=True)
    is_first = models.BooleanField()
    class Meta(object):
        db_table='videos_gotaward'


class ReviewTitle(models.Model):
    title = models.CharField(max_length=200)
    review = models.OneToOneField(Review, null=True,default=None,blank=True)
    class Meta(object):
        db_table='videos_reviewtitle'

def t():
    u = UserProfile.objects.get(id=2)

def create_badges():
    pass

class BadgeOptions(object):
    options = []


def get_badge_image(value):
    badge_images = {
        '5blue': '/static/badges/5badge.png',
        '5green': '/static/badges/5BadgeGreen.png',
        '5orange': '/static/badges/5BadgeOrange.png',
        '10blue': '/static/badges/10Badge.png',
        '10green': '/static/badges/10BadgeGreen.png',
        '10orange': '/static/badges/10BadgeOrange.png',
        '50blue': '/static/badges/50Badge.png',
        '100blue': '/static/badges/100Badge.png',
        '100orange': '/static/badges/100BadgeOrange.png',
        '100red': '/static/badges/100BadgeRed.png',
        'joined': '/static/badges/JoinedBadge.png',
        'watch2': '/static/badges/MediumWatchBadge.png',
        'pop1': '/static/badges/PopStar1.png',
        'pop2': '/static/badges/PopStar3.png',
        'watch1': '/static/badges/WatchBadge.png',
        'watch3': '/static/badges/SuperWatchBadge.png',
    }
    #example get_badge_image('pop1')
    return badge_images[value]