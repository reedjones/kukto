# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.conf.urls import url

from django.conf.urls import patterns
from kukto.profiles.views import register, people_index, user_login, user_logout, bad_login, my_profile,public_profile

urlpatterns = patterns('',
                       url(r'^$', people_index),
                       # ex: /serialy/family-guy
                       (r'^registerovat/$', register),
                       (r'^prihlasit/$', user_login),
                       (r'^odhlasit/$', user_logout),
                       (r'^omyl/$', bad_login),
                       (r'^muj_profile/$', my_profile),
                       (r'^uzivatelsky-profil/$',public_profile),

)
