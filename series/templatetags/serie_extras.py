# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_hooks()
from django import template
# Create your views here.
register = template.Library()
from kukto.series.models import NewShow
from kukto.Schemas.models import TVSeries,Movie
import re
from django.db.models import Avg, Count



@register.filter(name='gen')
def gen(s):
    return s.replace('_', ' ').replace('/', '').replace('`', '').replace('', '').replace('', '').replace('-',
                                                                                                         ' ').replace(
        ')', '').replace('(', '').replace('*', '').replace(',', '').replace('#', '').replace('!', '').replace('.',
                                                                                                              '').replace(
        '?', '').replace('$', '').replace('\'', '').replace(':', '').replace(' ', '-').replace('---', '-').replace('--',
                                                                                                                   '-').replace(
        '----', '-')


@register.filter(name='czechgen')
def czechgen(s):
    return s.replace('_', ' ').replace('/', '').replace('`', '').replace('', '').replace('', '').replace('-',
                                                                                                         ' ').replace(
        ')', '').replace('(', '').replace('*', '').replace(',', '').replace('#', '').replace('!', '').replace('.',
                                                                                                              '').replace(
        '?', '').replace('$', '').replace('\'', '').replace(':', '').replace(' ', '-').replace('---', '-').replace('--',
                                                                                                                   '-').replace(
        '----', '-').replace('Á', 'A').replace('á', 'a').replace('Č', 'C').replace('č', 'c').replace('Ď', 'D').replace(
        'ď', 'd').replace('É', 'E').replace('é', 'e').replace('Ě', 'E').replace('ě', 'e').replace('Í', 'I').replace('í',
                                                                                                                    'i').replace(
        'Ž', 'Z').replace('ž', 'z').replace('Ý', 'Y').replace('ý', 'y').replace('Ú', 'U').replace('ú', 'u').replace('Ů',
                                                                                                                    'U').replace(
        'ů', 'u').replace('Ť', 'T').replace('ť', 't').replace('Š', 'S').replace('š', 's').replace('Ř', 'R').replace('ř',
                                                                                                                    'r').replace(
        'Ó', 'O').replace('ó', 'o').replace('Ň', 'N').replace('ň', 'n')


@register.filter(name='startwith')
def startwith(s, arg):
    if s.startswith(arg):
        return True
    else:
        return False


def is_frame(value):
    if value[0:8] == "<iframe>":
        return True
    else:
        return False


def get_show_image(model, term):
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


def get_image_by_id(i):
    return NewShow.objects.get(id=i).image


@register.filter(name='get_image')
def get_image(value):
    #return get_show_image(NewShow, value.title).image
    return get_image_by_id(value)


@register.filter(name='startwithnumber')
def startwith(s):
    if s.startswith('#') or s.startswith('-') or s.startswith('$') or s[0].isdigit():
        return True
    else:
        return False


@register.filter(name='letters')
def startwith(s, arg):
    return bool(re.match(arg, s, re.I))


@register.filter(name='episode_get')
def episode_get(value):
    return value[3:4]


@register.filter(name='serie_get')
def serie_get(value):
    return value[0:1]


def check_string(v):
    if type(v) is str:
        return v + ','
    else:
        return str(v) + ','


@register.filter(name='comma')
def comma(value):
    return check_string(value)


def check_image(value):
    if 'http' in value or 'https' in value or '.com' in value:
        x = True
    else:
        x = False
    if x:
        return value
    else:
        return '/media/people/' + value

def check_image_two(value):
    if 'http' in value or 'https' in value or '.com' in value:
        return value
    else:
        return '/static/tv/'+value


def check_image_3(value):
    if 'http' in value or 'https' in value or '.com' in value:
        return value
    else:
        return 'http://kukto.cz/static/tv/'+value


@register.filter(name='get_tv_image_full_path')
def get_tv_image_full_path(value):
    return check_image_3(value)


@register.filter(name='get_tv_image')
def get_tv_image(value):
    return check_image_two(value)

@register.filter(name='person_image')
def person_image(value):
    return check_image(value)


def check_org_image(value):
    if 'http' in value or 'https' in value or '.com' in value:
        x = True
    else:
        x = False
    if x:
        return value
    else:
        return '/media/orgs/' + value


@register.filter(name='org_image')
def org_image(value):
    return check_org_image(value)


@register.filter(name='cz_genre')
def cz_genres(value):
    return value.replace("Action", "Akční").replace("action", "Akční").replace("Mystery", "Mysteriózní").replace(
        "Musical", "Muzikál").replace("Crime", "Krimi").replace("Adventure", "Dobrodružný").replace("Comedy", "Komedie")



import random
def from_rand(value):
    c = random.choice([1,2,3])
    if c == 1:
        return value
    elif c == 2:
        return value.replace('serial','<a href="http://kukto.cz/serialy/">serial</a>') #and so on
    else:
        return value



@register.filter(name="linked")
def linked(value):
    return from_rand(value)

def avg_rater(i,is_show):
    if is_show == 'film':
        show = Movie.objects.get(id=i)
    else:
        show = TVSeries.objects.get(id=i)
    avg_rate = show.aggregate_rating.all().aggregate(Avg('ratingValue'))
    if avg_rate['ratingValue__avg'] is not None:
        if type(avg_rate) is not int:
            avg_rate = int(avg_rate['ratingValue__avg'])
    else:
        avg_rate = 0
    return avg_rate


@register.filter(name='get_avg_rate')
def get_avg_rate(i,is_show):
    return avg_rater(i,is_show)


@register.filter(name='has_reviewed')
def has_reviewed(value):
    pass


@register.filter(name='cz_months')
def cz_months(value):
    print(value)
    return value.replace("March", "březen").replace("march", "březen").replace("January", "leden").replace("january",
                                                                                                           "leden").replace(
        "February", "únor").replace("february", "únor").replace("April", "duben").replace("april", "duben").replace(
        "May", "květen").replace("may", "květen").replace("June", "červen").replace("june", "červen").replace("July",
                                                                                                              "červenec").replace(
        "july", "červenec").replace("August", "srpen").replace("august", "srpen").replace("September", "září").replace(
        "september", "září").replace("October", "říjen").replace("october", "říjen").replace("November",
                                                                                             "listopad").replace(
        "november", "listopad").replace("December", "prosinec").replace("december", "prosinec")


    #.replace("midnight","").replace"Monday","pondělí").replace("Tuesday","úterý").replace("Wednesday","středa").replace("Thursday","čtvrtek").replace("Friday","pátek").replace("Saturday","sobota").replace("Sunday","neděle")