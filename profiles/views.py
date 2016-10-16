# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from kukto.actions.models import UserMadeReview
import datetime
from kukto.forms import UserForm, UserProfileForm
from kukto.profiles.models import UserProfile
from kukto.theviews.models import UserViewed
from django.shortcuts import render
from kukto.Schemas.models import Movie,TVSeries, Episode
from kukto.videos.models import BadgeGeneric,GotAward


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,'profiles/register.html',{
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered

    })


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next_url']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next_url)
            else:
                messages.add_message(request, messages.ERROR, 'Chybné přihlašovací')
                return HttpResponseRedirect('/lidi/prihlasit/')

        else:
            #bad credentials
            messages.add_message(request, messages.ERROR, 'Chybné přihlašovací jméno nebo heslo')
            return HttpResponseRedirect('/lidi/prihlasit/')

    next_url = request.GET.get('next')
    activate = request.GET.get('activate')
    activation = False
    uid = None
    if activate is not None:
        activation = True
        uid = request.GET['uid']


    return render(request,'profiles/login.html',{
        'next_url':next_url,
        'activation':activation,
        'uid':uid
    })


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    messages.add_message(request, messages.INFO, 'You are logged-out')
    return HttpResponseRedirect('/')


def bad_login(request):
    t = get_template('profiles/invalid_login.html')
    html = t.render(Context({

    }))
    return HttpResponse('hello')


def people_index(request):
    return HttpResponse()


@login_required
def my_profile(request):
    if request.method == 'POST':
        url = '/lidi/muj_profile/'
        if 'password' in request.POST:
            p = request.POST['password']
            u = request.user
            u.set_password(p)
            u.save()
            messages.add_message(request,messages.SUCCESS,'informace byly úspěšně přidány')
            return HttpResponseRedirect(url)
        if 'username' in request.POST:
            un =request.POST['username']
            u = request.user
            u.username = un
            u.save()
            messages.add_message(request,messages.SUCCESS,'informace byly úspěšně přidány')
            return HttpResponseRedirect(url)
        if 'picture' in request.FILES:
            profile = UserProfile.objects.get(user=request.user)
            profile.picture = request.FILES['picture']
            profile.save()
            messages.add_message(request,messages.SUCCESS,'informace byly úspěšně přidány')
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/')
    else:
        logout = request.GET.get('logout')
        if logout == 1:
            logout(request)
            messages.add_message(request, messages.INFO, 'You are logged-out')
            return HttpResponseRedirect('/')

        profile = UserProfile.objects.get(user=request.user) #.select_related()
        rated_series = profile.rated_series.all() #this can be in template
        rated_films = profile.rated_movies.all()
        rated_episode = profile.rated_episodes.all()
        liked_films = profile.liked_movies.all()
        liked_shows = profile.liked_series.all()
        last = request.user.last_login

        latest_films = Movie.objects.filter(new_movie__date__range=[last,datetime.date.today()])
        latest_shows = TVSeries.objects.filter(new_show__date__range=[last,datetime.date.today()])

        reviews = UserMadeReview.objects.filter(user_profile=profile)

        s_reviews = reviews.filter(is_show=True)
        f_reviews = reviews.filter(is_film=True)

        series_que = []
        qued_shows = profile.que_series.all()[:10]
        for i in qued_shows:
            latest_episode = Episode.objects.filter(partOfSeries=i).order_by('new_episode__date')[0]
            last_view_date = UserViewed.objects.filter(is_show=True).filter(obj_id=i.id).order_by('date')[0]
            #be sure to update
            watched = profile.watched_episodes.filter(id=latest_episode.id).exists()
            series_que.append(
                {
                    'show':i,
                    'last_view':last_view_date,
                    'latest_episode':latest_episode,
                    'watched':watched
                }
            )


        #Episode.objects.filter(partOfSeries=show).order_by('new_episode__date')
        #UserWat
        num_series = profile.watched_series.count()
        num_films = profile.watched_movies.count()
        num_episodes = profile.watched_episodes.count()


        return render(request,'profiles/myprofile.html',{
            'profile': profile,
            'rated_series': rated_series,
            'rated_films': rated_films,
            'rated_episodes': rated_episode,
            'liked_films': liked_films,
            'liked_shows': liked_shows,
            'reviews': reviews,
            's_reviews': s_reviews,
            'f_reviews': f_reviews,
            'latest_films':latest_films,
            'latest_shows':latest_shows,
            'num_series':num_series,
            'num_episodes':num_episodes,
            'num_films':num_films,
            'series_que':series_que


        })




def public_profile(request):
    i = request.GET['id']
    profile = UserProfile.objects.get(id=i)
    the_user = profile.user
    #profile = UserProfile.objects.get(user=request.user) #.select_related()
    rated_series = profile.rated_series.all() #this can be in template
    rated_films = profile.rated_movies.all()
    rated_episode = profile.rated_episodes.all()
    liked_films = profile.liked_movies.all()
    liked_shows = profile.liked_series.all()
    last = request.user.last_login

    latest_films = Movie.objects.filter(new_movie__date__range=[last,datetime.date.today()])
    latest_shows = TVSeries.objects.filter(new_show__date__range=[last,datetime.date.today()])

    reviews = UserMadeReview.objects.filter(user_profile=profile)

    s_reviews = reviews.filter(is_show=True)
    f_reviews = reviews.filter(is_film=True)
    num_series = profile.watched_series.count()
    num_films = profile.watched_movies.count()
    num_episodes = profile.watched_episodes.count()

    return render(request, 'profiles/public_profile.html', {
        'the_user':the_user,
        'profile': profile,
        'rated_series': rated_series,
        'rated_films': rated_films,
        'rated_episodes': rated_episode,
        'liked_films': liked_films,
        'liked_shows': liked_shows,
        'reviews': reviews,
        's_reviews': s_reviews,
        'f_reviews': f_reviews,
        'latest_films':latest_films,
        'latest_shows':latest_shows,
        'num_series':num_series,
        'num_episodes':num_episodes,
        'num_films':num_films,
        #'series_que':series_que


    })

def whole_que(request):
    profile = UserProfile.objects.get(user=request.user) #.select_related()
    series_qu = []
    qued_shows = profile.que_series.all()
    for i in qued_shows:
        latest_episode = Episode.objects.filter(partOfSeries=i).order_by('new_episode__date')[0]
        last_view_date = UserViewed.objects.filter(is_show=True).filter(obj_id=i.id).order_by('date')[0]
        #be sure to update
        watched = profile.watched_episodes.filter(id=latest_episode.id).exists()
        series_qu.append(
            {
                'show':i,
                'last_view':last_view_date,
                'latest_episode':latest_episode,
                'watched':watched
            }
        )
    pagnation = Paginator(series_qu, 9)
    page = request.GET.get('page')
    try:
        series_que = pagnation.page(page)
    except PageNotAnInteger:
        series_que = pagnation.page(1)
    except EmptyPage:
        series_que = pagnation.page(pagnation.num_pages)

    return render(request,'profiles/snippits/que.html',{'series_que':series_que})


