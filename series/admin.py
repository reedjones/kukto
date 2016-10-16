# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django.contrib import admin
from kukto.series.models import NewEpisode, NewEpisodeAdmin, NewMovie, NewMovieAdmin, NewShow, NewShowAdmin

# Register your models here.


admin.site.register(NewEpisode, NewEpisodeAdmin)
admin.site.register(NewShow, NewShowAdmin)
admin.site.register(NewMovie, NewMovieAdmin)
