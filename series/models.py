# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from future.builtins import object
from django.db import models
from django.contrib import admin


class ShowMeta(models.Model):
    id = models.AutoField(primary_key=True, max_length=255, db_column="id")
    show_title = models.TextField(db_column="show_title")
    watch_count = models.IntegerField(db_column="watch_count")
    likes = models.IntegerField(db_column="likes")

    class Meta(object):
        db_table = 'show_meta'

    def __str__(self):
        return self.show_title

    def watched(self):
        self.watch_count += 1

    def liked(self):
        self.likes += 1

    def get_likes(self):
        return self.likes

    def counts(self):
        return self.watch_count


class MovieMeta(models.Model):
    id = models.AutoField(primary_key=True, max_length=255, db_column="id")
    movie_title = models.TextField(db_column="movie_title")
    watch_count = models.IntegerField(db_column="watch_count")
    likes = models.IntegerField(db_column="likes")

    class Meta(object):
        db_table = 'movie_meta'

    def __str__(self):
        return self.movie_title

    def watched(self):
        self.watch_count += 1

    def liked(self):
        self.likes += 1

    def get_likes(self):
        return self.likes

    def counts(self):
        return self.watch_count


class NewShow(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    title = models.TextField(db_column="title")
    description = models.TextField(db_column="description")
    image = models.TextField(db_column="image")
    date = models.DateTimeField(db_column='date', auto_now=True)


    class Meta(object):
        db_table = 'new_show'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.description


class NewEpisode(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")

    title = models.TextField(db_column="title")

    link = models.TextField(db_column="link")

    show_title = models.TextField(db_column="show_title")  #related_name='entries'

    date = models.DateTimeField(db_column='date', auto_now=True)

    class Meta(object):
        db_table = 'new_episode'

    def __str__(self):
        return self.title


class NewMovie(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    title = models.TextField(db_column="title")
    description = models.TextField(db_column="description")
    image = models.TextField(db_column="image")
    genera = models.TextField(db_column="genera")
    frame = models.TextField(db_column="frame")
    date = models.DateTimeField(db_column='date', auto_now=True)

    class Meta(object):
        db_table = 'new_movie'

    def __str__(self):
        return self.title


class NewShowAdmin(admin.ModelAdmin):
    list_display = ('title',)


class NewEpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_title')


class NewMovieAdmin(admin.ModelAdmin):
    list_display = ('title',)









    




    
    
     
