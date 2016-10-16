# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.conf.urls import url

from kukto.movies.views import film_index, film_genera, film, all_films

from django.conf.urls import patterns


urlpatterns = patterns('',

                       url(r'^$', film_index),

                       #(r'^(?P<movie_genera>[-\w]+)/$', film_genera),

                       (r'^vsechny/$', all_films),

                       (r'^zanry/(?P<movie_genera>[-\w]+)/$', film_genera),

                       #(r'^databaze/(?P<movie_title>[-\w]+)/$', film_info),

                       (r'^sledovat/(?P<movie_title>[-\w]+)/(?P<movie_id>\d+)/$', film),


)
