# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.conf.urls import url

from kukto.series import views
from kukto.series.views import serial, episode, all_series

from django.conf.urls import patterns


urlpatterns = patterns('',

                       url(r'^$', views.serialy_index, name='serialy_index'),
                       # ex: /serialy/family-guy

                       (r'^vsechny/$', all_series),


                       (r'^(?P<serial_title>[-\w]+)/$', serial),

                       (r'^(?P<serial_title>[-\w]+)/(?P<episode_title>[-\w]+)/$', episode),


)


