# -*- coding: utf-8 -*-
import json

from django.http import HttpResponseRedirect, HttpResponse
from haystack.query import SearchQuerySet
from django.template.loader import render_to_string, get_template
from django.template import Context


def search_films(request):
    try:
        term = request.GET['q']
    except:
        return HttpResponseRedirect('/')

    results = SearchQuerySet().auto_query(term)
    films = []
    for r in results:
        films.append(r.object)

        return HttpResponse(films)


def ajax_films(request):
    term = request.GET['q']
    if not term:
        print('bad')
    else:
        results = SearchQuerySet().auto_query(term)
        films = []
        for r in results:
            films.append(r.object)

        html = render_to_string('search/search2.html', {'objects': films})
        res = {'html': html}
        return HttpResponse(json.dumps(res), content_type='application/json')


def p_films(request):
    #SearchQuerySet().filter(content='harry')
    term = request.POST['q']
    results = SearchQuerySet().auto_query(term)

    t = get_template('search/search.html')
    html = t.render(Context({
        'objects': results
    }))
    return HttpResponse(html)


def get_related(request):
    #x = SearchQuerySet().more_like_this(Object-here)
    pass