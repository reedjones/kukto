# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from django.db.models import Avg, Count
from future.builtins import int
from future import standard_library
from kukto.profiles.models import UserProfile
from kukto.theviews.models import UserViewed
standard_library.install_hooks()
from kukto.Schemas.models import TVSeries, Episode, Movie, Review, View
from kukto.actions.models import UserMadeReview
from kukto.series.models import NewEpisode
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.http import HttpResponseRedirect
from kukto.ajax.models import EpisodeRating
#from django.template.context import RequestContext
from datetime import date
#from django.shortcuts import render_to_response,redirect
from django.shortcuts import render
from kukto.videos.models import EpisodeVideoObj



def strip(s):
    return s.replace('-', ' ')


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def filter_or_none(model, **kwargs):
    try:
        return model.objects.filter(**kwargs)
    except model.DoesNotExist:
        return None


def get_show(model, term):
    try:
        return model.objects.get(title__iexact=term)
    except model.DoesNotExist:
        try:
            return model.objects.get(title__icontains=term)
        except:
            try:
                if len(model.objects.get(title__icontains=term)) < 2:
                    return model.objects.filter(title__icontains=term)[0]
            except:
                return None


def get_tv_show(model, term):
    try:
        return model.objects.get(name__iexact=term)
    except model.DoesNotExist:
        try:
            return model.objects.get(name__icontains=term)
        except:
            try:
                if len(model.objects.get(name__icontains=term)) < 2:
                    return model.objects.filter(name__icontains=term)[0]
            except:
                return None


def get_episode(s, e):
    try:
        obj = Episode.objects.filter(new_episode__show_title__icontains=s).filter(title__startswith=e[0:5])
        if len(obj) > 2:
            obj = obj[0]
            return obj
        else:
            return obj
    except NewEpisode.DoesNotExist:
        return None


def all_series(request):
    obj = TVSeries.objects.all().order_by('name')
    s1 = obj[0:int(obj.count() / 3)]
    s2 = obj[int(obj.count() / 3):int(obj.count() / 3) + int(obj.count() / 3)]
    s3 = obj[
         int(obj.count() / 3) + int(obj.count() / 3):int(obj.count() / 3) + int(obj.count() / 3) + int(obj.count() / 3)]


    return render(request,'series/all-series.html',{
        'shows_one': s1,
        'shows_two': s2,
        'shows_three': s3

    })


def serialy_index(request):
    o = TVSeries.objects.all().order_by('new_show__title')
    new = Episode.objects.all().order_by('-new_episode__date').select_related('partOfSeries')#.prefetch_related()
    unique = []
    a = []
    for item in new:
        if item.partOfSeries.id not in a:
            unique.append(item)
            a.append(item.partOfSeries.id)

    pagnation = Paginator(unique, 9)
    page = request.GET.get('page')
    try:
        newest = pagnation.page(page)
    except PageNotAnInteger:
        newest = pagnation.page(1)
    except EmptyPage:
        newest = pagnation.page(pagnation.num_pages)
    p = TVSeries.objects.all().annotate(num_views=Count('views')).order_by('num_views')[:10]

    pop_show = random.choice(p)
    recent_shows = TVSeries.objects.all().order_by('-new_show__date')[:2]


    return render(request, 'series/series.html',{'popular_show': pop_show,
        'recent_shows': recent_shows,
        'new_episodes': newest,
        'all_shows': o})


def serial(request, serial_title=None):
    show_id = request.GET.get('id')
    if id is None:
        s_title = strip(serial_title)
        obj = get_tv_show(TVSeries, s_title)
        if obj is None:
            return HttpResponse('/serialy/') #Check this
    else:
        obj = TVSeries.objects.get(id=show_id) ##CHECK THIS

    if request.user.is_authenticated():
        today = date.today()
        profile = UserProfile.objects.get(user=request.user)
        if not profile.watched_series.filter(id=obj.id).exists():
            profile.watched_series.add(obj)
        if not UserViewed.objects.filter(is_show=True).filter(obj_id=obj.id).filter(date__year=today.year).filter(date__month=today.month).filter(date__day=today.day).exists():
            uvo = UserViewed(is_show=True,obj_id=obj.id,is_movie=False,is_episode=False,user=profile)
            uvo.save()
    else:
        #just a regular view
        v = View(view_count=1)
        v.save()
        obj.views.add(v)

    show_episodes = obj.episode_set.all().order_by('partOfSeason__number', 'episodeNumber')
    reviewed = UserMadeReview.objects.filter(is_show=True).filter(obj_id=show_id)
    des = obj.new_show.description
    img = obj.new_show.image
    title = obj.new_show.title

    number_of_ratings = obj.aggregate_rating.all().count()
    if number_of_ratings > 0:
        avg_rate = obj.aggregate_rating.all().aggregate(Avg('ratingValue'))
        if avg_rate['ratingValue__avg'] is not None:
            if type(avg_rate) is not int:
                avg_rate = int(avg_rate['ratingValue__avg'])
        else:
            avg_rate = 0
    else:
        avg_rate = 0

    if request.user.is_authenticated():
        review_tip = 'napsat recenzi '
    else:
        review_tip = 'pro tuto činnost se musíte registrovat'


    return render(request,'series/show2.html',{
        'obj': obj,
        'the_title': title,
        'the_image': img,
        'the_description': des,
        'show_episode_list_first': show_episodes,
        #'show_episode_list_second': s2,
        'avg_rate': avg_rate,
        'review_tip': review_tip,
        'number_of_ratings': number_of_ratings,
        'reviewed': reviewed
    })


def episode(request, serial_title=None, episode_title=None):
    e_id = request.GET.get('id')
    if e_id is not None:
        obj = Episode.objects.get(id=e_id)
        episode_link = obj.new_episode.link
    else:
        e_title = strip(episode_title)
        s_title = strip(serial_title)
        obj = get_episode(s_title, e_title)
        if obj is not None:
            try:
                episode_link = obj.new_episode.link
            except:
                episode_link = obj[0].new_episode.link
        else:
            return HttpResponseRedirect('/')

    if request.user.is_authenticated():
        profile = UserProfile.objects.get(user=request.user)
        if not profile.watched_episodes.filter(id=obj.id).exists():
            profile.watched_episodes.add(obj)

    if '<iframe' in episode_link[0:7]:
        frame = True
    else:
        frame = False

    number_of_episodes = obj.partOfSeries.episode_set.all().count()

    r = UserMadeReview.objects.filter(is_episode=True, obj_id=obj.id)

    if request.user.is_authenticated():
        profile = UserProfile.objects.get(user=request.user)
        if not profile.watched_episodes.filter(id=obj.id).exists():
            profile.watched_episodes.add(obj)
    v = View(view_count=1)
    v.save()
    obj.views.add(v)

    #avg_rate = obj.aggregate_rating.all().aggregate(Avg('ratingValue'))
    if EpisodeRating.objects.filter(episode=obj).exists():
        avg_rate = EpisodeRating.objects.filter(episode=obj).aggregate(Avg('rating__ratingValue'))
        if avg_rate['rating__ratingValue__avg'] is not None:
            if type(avg_rate) is not int:
                avg_rate = int(avg_rate['rating__ratingValue__avg'])
        else:
            avg_rate = 0
    else:
        avg_rate = 0

    number_of_ratings = EpisodeRating.objects.filter(episode=obj)
    unique_ratings = []
    go_count = 0
    num = number_of_ratings.count()
    while go_count < num:
        current = number_of_ratings[go_count]
        print(current.user.username)
        if unique_ratings:
            already_in = False
            for rr in unique_ratings:
                #print('checking against %s' %current.user.username+' '+rr.user.username)
                if current.user.username == rr.user.username:
                    already_in = True
            if already_in:
                pass
            else:
                #print('adding into %s'+current.user.username)
                unique_ratings.append(current)
        else:
            #print('added first')
            unique_ratings.append(current)
        go_count+=1



    videoObj = EpisodeVideoObj.objects.filter(episode=obj).all()



    return render(request,'series/svideo.html',{
        'is_iframe': frame,
        'the_episode_link': episode_link,
        'episode': obj,
        'numer_of_episodes': number_of_episodes,
        'reviewed': r,
        'avg_rate': avg_rate,
        'number_of_ratings': unique_ratings,
        'alt_videos':videoObj,
    })


def home_index(request):
    if request.GET.get('ahoj'):
        first = True
    else:
        first = False

    #pop_shows = TVSeries.objects.all().annotate(num_views=Count('views')).order_by('num_views')[:10]

    recent_shows = TVSeries.objects.all().order_by('-new_show__date')[:2]

    recent_films = Movie.objects.all().order_by('-new_movie__date')[:10]

    #pop_films = Movie.objects.all().annotate(num_views=Count('views')).order_by('num_views')[:10]

    recent_reviews = Review.objects.all().order_by('date_reviewed')[:20]


    return render(request,'home.html',{
        'recent_films': recent_films,
        'recent_shows': recent_shows,
        'recent_reviews': recent_reviews,
        'm': first


    })


def podminky(request):
    t = get_template('podminky.html')
    return render(request,'podminky.html',{})
