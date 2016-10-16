# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future.builtins import int
from future import standard_library

standard_library.install_hooks()
from kukto.profiles.models import UserProfile
from kukto.Schemas.models import Movie, View
from kukto.actions.models import UserMadeReview
from kukto.series.views import strip
from django.shortcuts import render
from django.db.models import Avg, Count
from django.template import Context
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse

import random


def no_digits(s):
    return ''.join(i for i in s if not i.isdigit())


def film_index(request):
    new = Movie.objects.all().exclude(new_movie__image='').order_by('-new_movie__date')

    pagnation = Paginator(new, 9)

    page = request.GET.get('page')
    try:
        newest = pagnation.page(page)
    except PageNotAnInteger:
        newest = pagnation.page(1)
    except EmptyPage:
        newest = pagnation.page(pagnation.num_pages)

    p = Movie.objects.all().annotate(num_views=Count('views')).order_by('num_views')[:10]
    #p = MovieMeta.objects.all().order_by('-watch_count')[:20]

    pop_show = random.choice(p)

    recent_shows = Movie.objects.all().exclude(new_movie__image='').order_by('-new_movie__date')[:2]

    return render(request, 'films/films.html', {
        'popular_film': pop_show,
        'recent_shows': recent_shows,
        'new_films': newest,

    })


def all_films(request):
    films = Movie.objects.all().exclude(new_movie__image='')
    rows = 3 * 12

    pagnation = Paginator(films, rows)

    page = request.GET.get('page')

    try:
        movies = pagnation.page(page)
    except PageNotAnInteger:
        movies = pagnation.page(1)
    except EmptyPage:
        movies = pagnation.page(pagnation.num_pages)

    return render(request, 'films/all_films.html', {
        'films': movies
    })


def film_genera(request, movie_genera=None):
    g = movie_genera
    o = Movie.objects.filter(new_movie__genera=g).exclude(new_movie__frame='None').exclude(
        new_movie__frame__contains='filman.cz').order_by('new_movie__title')

    rows = 3 * 12
    pagnation = Paginator(o, rows)

    page = request.GET.get('page')
    try:
        films = pagnation.page(page)
    except PageNotAnInteger:
        films = pagnation.page(1)
    except EmptyPage:
        films = pagnation.page(pagnation.num_pages)

    return render(request, 'films/filmstyle.html', {

        #'film_list':o
        'films': films,
        'genera': g

    })


def film(request, movie_title=None, movie_id=None):
    tit = strip(movie_title)
    i_film = True
    sid = movie_id
    una = True
    if not sid:
        sid = request.GET.get('id')
        if not sid:
            try:
                the_film = Movie.objects.filter(name=tit).exclude(frame='None').exclude(frame__contains='filman.cz')[0]
            except Movie.DoesNotExist:
                return HttpResponseRedirect('/filmy/')
        else:
            the_film = Movie.objects.get(id=sid)
    else:
        the_film = Movie.objects.get(id=sid)

    if request.user.is_authenticated():
        profile = UserProfile.objects.get(user=request.user)
        review_tip = 'napsat recenze'
        una = False
        if not profile.watched_movies.filter(id=the_film.id).exists():
            profile.watched_movies.add(the_film)
    else:
        review_tip = 'musite prihlasit'

    if the_film.new_movie.frame is None:
        i_film = False
    else:
        if 'http://filman.cz' in the_film.new_movie.frame:
            i_film = False

    the_image = the_film.new_movie.image
    the_description = the_film.new_movie.description
    if '</span>' in the_description:
        #the_description.replace('<','').replace('>','').replace('span','').replace('id','').replace('class','').replace('more','').replace('-','').replace('/','')
        the_description = ''
    the_title = the_film.new_movie.title
    the_genera = the_film.new_movie.genera
    the_frame = the_film.new_movie.frame

    reviewed = UserMadeReview.objects.filter(is_film=True, obj_id=the_film.id)
    v = View(view_count=1)
    v.save()
    the_film.views.add(v)

    number_of_ratings = the_film.aggregate_rating.all().count()
    if number_of_ratings > 0:
        avg_rate = the_film.aggregate_rating.all().aggregate(Avg('ratingValue'))
        if avg_rate['ratingValue__avg'] is not None:
            if type(avg_rate) is not int:
                avg_rate = int(avg_rate['ratingValue__avg'])
        else:
            avg_rate = 0
    else:
        avg_rate = 0

    return render(request, 'films/fvideo.html', {

        'is_film': i_film,
        'the_title': the_title,
        'the_description': the_description,
        'the_genera': the_genera,
        'the_image': the_image,
        'the_frame': the_frame,
        'film': the_film,
        'reviewed': reviewed,
        'user_not_auth': una,
        'avg_rate': avg_rate,
        'number_of_ratings': number_of_ratings,
        'review_tip': review_tip,


    })


#@login_required
def add_video(request):
    fid = request.GET['id']
    obj = Movie.objects.get(id=fid)











