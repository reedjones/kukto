# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.conf.urls import patterns, url
from kukto.Schemas import views


urlpatterns = patterns('',

                       url(r'^search_films/$', views.search_films),

                       url(r'^ajax_films/$', views.ajax_films),

                       url(r'^post_films/$', views.p_films),

)


