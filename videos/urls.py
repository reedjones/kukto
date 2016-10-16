from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.conf.urls import url, patterns
from kukto.videos.views import add_episode_link


urlpatterns = patterns('',

                       url(r'^add_episode_link/$', add_episode_link),



)
