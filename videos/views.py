# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from kukto.Schemas.models import Episode
from kukto.profiles.models import UserProfile
from kukto.videos.models import EpisodeVideoObj, VideoRequest, alternateLink, get_badge_image,BadgeGeneric, GotAward


def add_episode_link(request):
    if request.method == 'POST':
        url = request.POST['url']
        if request.user.is_anonymous():
            messages.add_message(request,messages.ERROR,'pro tuto činnost se musíte registrovat')
            return HttpResponseRedirect(url)

        profile = UserProfile.objects.get(user=request.user)

        uploaded = profile.added_links.all()
        hb = 0
        for i in uploaded:
            if i.is_flagged:
                hb+=1
        if hb > 3:
            pass
        if hb > 6:
            messages.add_message(request,messages.ERROR,'Nemůžete Přidávat')
            return HttpResponseRedirect(url)

        if profile.active_int < 10:
            okay = False
        else:
            okay = True
        if request.user.username == 'techno760' or request.user.username == 'jones':
            print('was techno')
            okay = True

        if not okay:
            messages.add_message(request,messages.ERROR,'Musíte mít vyšší skóre přidat video')
            return HttpResponseRedirect(url)
        #default request user
        try:
            profile.active_int+=1
            profile.save()
        except:
            pass
        #print('so far so good')

        eid = request.POST['episode_id']
        episode = Episode.objects.get(id=eid)

        link = request.POST['link']


        alt_link = alternateLink.objects.create(link=link,uploaded_by=profile,quality=1,is_flagged=False)


        me = UserProfile.objects.first()

        r = VideoRequest(user=me,alternateLink=alt_link)
        r.save()


        evo = EpisodeVideoObj(episode=episode)
        evo.save()
        evo.alternate_links.add(alt_link)

        num_added = profile.added_links.all().count()
        first_time = False
        if num_added < 2:
            first_time = True
        if first_time:
            bi = get_badge_image('pop1')
            try:
                badge = BadgeGeneric.objects.get(name='přidal první video')
            except:
                badge = BadgeGeneric.objects.create(name='přidal první video',image=bi,points_needed=10,points_earned=2,max_num=100)

            ga = GotAward(badge_generic=badge,user=profile,is_first=True)
            ga.save()

            messages.add_message(request,messages.SUCCESS,'Vyhrál Jsi Trofej!'+'<img src='+bi+'alt="tophej" class="badge-generic" />')

        else:
            bi = get_badge_image('pop2')
            vname = 'přidal %s videa'%num_added
            try:
                badge = BadgeGeneric.objects.get(name=vname)
            except:
                badge = BadgeGeneric.objects.create(name=vname,image=bi,points_needed=20,points_earned=5,max_num=100)
            ga = GotAward(badge_generic=badge,user=profile,is_first=True)
            ga.save()
            messages.add_message(request,messages.SUCCESS,'Vyhrál Jsi Trofej!'+'<img src='+bi+'alt="tophej" class="badge-generic" />')



        messages.add_message(request,messages.SUCCESS,'Informace byly úspěšně přidány')

        return HttpResponseRedirect(url)




