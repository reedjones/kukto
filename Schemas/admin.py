# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.contrib import admin
from kukto.Schemas.models import TVSeries, TVSeriesAdmin, Episode, EpisodeAdmin, Movie, MovieAdmin, Person, PersonAdmin, Keyword, KeywordAdmin, VideoObject, VideoObjectAdmin, Season, SeasonAdmin


admin.site.register(Movie, MovieAdmin)
admin.site.register(TVSeries, TVSeriesAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(VideoObject, VideoObjectAdmin)
admin.site.register(Season, SeasonAdmin)
