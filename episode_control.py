from django.db.utils import IntegrityError

from kukto.series.models import NewEpisode, NewShow
from kukto.Schemas.models import Season, Episode, TVSeries


def do_it():
    all_episodes = NewEpisode.objects.all()

    i = 0
    count = all_episodes.count()

    while i < count:
        current = all_episodes[i]
        try:
            n = NewShow.objects.get(title=current.show_title)
            pos = TVSeries.objects.get(new_show=n)
            num = int(current.title[0:2])
            season = Season(partOfSeries=pos, number=num)
            season.save()
            episode = Episode(episodeNumber=int(current.title[3:5]),
                              partOfSeason=season,
                              partOfSeries=pos,
                              new_episode=current,
                              name=current.title,

            )
            episode.save()
        except (NewShow.DoesNotExist, IntegrityError):
            print('no show found matching query')
        i += 1
        print(i, ' out of ', count, ' episodes completed')









