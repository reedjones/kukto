# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future.builtins import object
from future import standard_library

standard_library.install_hooks()

from django.db import models
from django.contrib import admin
from kukto.imdb.models import Movies
from kukto.series.models import NewShow, NewMovie, NewEpisode


class MusicGroup(models.Model):
    name = models.CharField(blank=True, default='', max_length=200)

    class Meta(object):
        db_table = 'music_group_schema'


class Keyword(models.Model):
    tag = models.SlugField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_keyword'


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('tag',)


class AggregateRating(models.Model):
    itemReviewed = models.TextField(blank=True, default='') #the item being reviewd should be Thing
    ratingCount = models.BigIntegerField(null=True, blank=True, default=None)
    reviewCount = models.BigIntegerField(null=True, blank=True, default=None)
    bestRating = models.IntegerField(null=True, blank=True, default=None)
    worstRating = models.IntegerField(null=True, blank=True, default=None)
    ratingValue = models.IntegerField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_aggregaterating'

class Rating(models.Model):
    bestRating = models.IntegerField(default=5)
    worstRating = models.IntegerField(default=1)
    ratingValue = models.IntegerField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_rating'

class Organization(models.Model):
    name = models.CharField(blank=True, default='', max_length=200)
    sameAs = models.URLField(null=True, blank=True, default=None)
    image = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')

    class Meta(object):
        db_table = 'schemas_organization'

class Country(models.Model):
    name = models.CharField(blank=True, default='', max_length=200)
    globalLocationNumber = models.BigIntegerField(null=True, blank=True, default=None)
    image = models.TextField(blank=True, default='')
    logo = models.TextField(blank=True, default='')

    class Meta(object):
        db_table = 'schemas_country'

class Person(models.Model):
    name = models.CharField(blank=True, default='', max_length=200)
    birthDate = models.DateField(null=True, blank=True, default=None)
    deathDate = models.DateField(null=True, blank=True, default=None)
    duns = models.TextField(blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')
    nationality = models.ForeignKey(Country, null=True, blank=True, default=None)
    sameAs = models.URLField(null=True, blank=True, default=None)
    images = models.TextField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_person'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)


class Image(models.Model):
    src = models.TextField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_image'

class Actor(Person):
    person_id = models.BigIntegerField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_actor'


class Review(models.Model):
    itemReviewed = models.TextField(blank=True, default='') #the item being reviewd should be Thing
    reviewBody = models.TextField(blank=True, default='')
    reviewRating = models.OneToOneField(Rating, null=True, blank=True, default=None)

    aggregate_rating = models.ManyToManyField(AggregateRating, null=True, blank=True, default=None,db_table='schemas_review_aggregate_rating')

    dateCreated = models.DateField(null=True, blank=True,
                                   default=None) #the thing that's being reviewd not the creation of the review
    date_reviewed = models.DateTimeField(auto_now=True)
    inLanguage = models.CharField(max_length=100, default='CS cz')
    interactionCount = models.CharField(max_length=200, blank=True, default='')
    keywords = models.ManyToManyField(Keyword, null=True, blank=True, default=None,db_table='schemas_review_keywords')

    class Meta(object):
        db_table = 'schemas_review'

class VideoObject(models.Model):
    productionCompany = models.ManyToManyField(Organization, null=True, blank=True, default=None,db_table='schemas_videoobject_productioncompany')
    #thumbnail = models.
    videoFrameSize = models.CharField(max_length=200, blank=True, default='')
    videoQuality = models.CharField(max_length=200, blank=True, default='')
    #duration = models.
    encodingFormat = models.CharField(max_length=100, blank=True, default='')
    interactionCount = models.CharField(max_length=200, blank=True,
                                        default='') #<meta itemprop="interactionCount" content="UserTweets:1203"/>
    uploadDate = models.DateTimeField(null=True, blank=True, default=None)
    name = models.TextField(blank=True, default='')
    aggregate_rating = models.ManyToManyField(AggregateRating, null=True, blank=True, default=None,db_table='schemas_videoobject_aggregate_rating')
    inLanguage = models.CharField(max_length=100, default='CS cz')
    embedUrl = models.TextField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_videoobject'

class VideoObjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta(object):
        db_table = 'schemas_genre'

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class View(models.Model):
    view_date = models.DateTimeField(auto_now=True)
    view_count = models.BigIntegerField()

    class Meta(object):
        db_table = 'schemas_view'

#### High Level Schema Objects
##------------------------------------------------------------

class TVBase(models.Model):
    views = models.ManyToManyField(View, null=True, blank=True, default=None,db_table='schemas_tvbase_views')

    actors = models.ManyToManyField(Person, null=True, blank=True, default=None,
                                    related_name='actors',db_table='schemas_tvbase_actors')
                                    #actors is just a list of people

    director = models.ManyToManyField(Person, null=True, blank=True, default=None, related_name='directors',db_table='schemas_tvbase_director')
    #episodes = models.Many

    writers = models.ManyToManyField(Person, null=True, blank=True, default=None, related_name='writers',db_table='schemas_tvbase_writers')

    cinematographers = models.ManyToManyField(Person, null=True, blank=True, default=None,
                                              related_name='cinematographers',db_table='schemas_tvbase_cinematographers')

    distributors = models.ManyToManyField(Organization, null=True, blank=True, default=None,
                                          related_name='distributors', db_table='schemas_tvbase_distributors')

    musicBy = models.ManyToManyField(Person, null=True, blank=True, default=None, related_name='musician',db_table='schemas_tvbase_musicby')

    musicByGroup = models.ManyToManyField(MusicGroup, null=True, blank=True, default=None, related_name='music_group',db_table='schemas_tvbase_musicbygroup')
    numberOfEpisodes = models.IntegerField(null=True, blank=True, default=None)

    producer = models.ManyToManyField(Person, null=True, blank=True, default=None, related_name='producer',db_table='schemas_tvbase_producer')

    datePublished = models.DateTimeField(null=True, blank=True, default=None)
    genre = models.ManyToManyField(Genre, null=True, default=None, blank=True,db_table='schemas_tvbase_genre')
    #genres = models.ManyToManyField(Genre,null=True, blank=True, default = None)
    inLanguage = models.CharField(max_length=200, default='Cs cz')
    interactionCount = models.CharField(max_length=200, default='', blank=True)
    likes = models.BigIntegerField(default=0)
    isFamilyFriendly = models.NullBooleanField()

    keywords = models.ManyToManyField(Keyword, null=True, blank=True, default=None,db_table='schemas_tvbase_keywords')
    review = models.ManyToManyField(Review, null=True, blank=True, default=None,db_table='schemas_tvbase_review')

    image = models.TextField(blank=True, default='')

    images = models.ManyToManyField(Image, null=True, blank=True, default=None, related_name='image_group',db_table='schemas_tvbase_images')
    videoObject = models.ManyToManyField(VideoObject, null=True, blank=True, default=None,db_table='schemas_tvbase_videoobject')

    alternateName = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
    name = models.CharField(max_length=200, blank=True, default='')
    sameAs = models.URLField(null=True, blank=True, default=None)
    aggregate_rating = models.ManyToManyField(AggregateRating, null=True, blank=True, default=None,
                                              related_name='ratings',db_table='schemas_tvbase_aggregate_rating')

    production_companies = models.ManyToManyField(Organization, null=True, blank=True, default=None,
                                                  related_name='production_companies',db_table='schemas_tvbase_production_companies')

    class Meta(object):
        db_table = 'schemas_tvbase'


class TVSeries(TVBase):
    #kukshow = models.OneToOneField(KukShow,null=True, blank=True, default = None)
    new_show = models.OneToOneField(NewShow, null=True, blank=True, default=None)
    imdb = models.OneToOneField(Movies, null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_tvseries'

class Movie(TVBase):
    is_czech = models.NullBooleanField()
    #kukmovie = models.OneToOneField(KukMovie,null=True, blank=True, default = None)
    new_movie = models.OneToOneField(NewMovie, null=True, blank=True, default=None)
    imdb = models.OneToOneField(Movies, null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_movie'

class Season(models.Model):
    numberOfEpisodes = models.IntegerField(null=True, blank=True, default=None)
    partOfSeries = models.ForeignKey(TVSeries, null=True, blank=True, default=None)
    startDate = models.DateField(null=True, blank=True, default=None)
    endDate = models.DateField(null=True, blank=True, default=None)
    number = models.IntegerField(null=True, blank=True, default=None)

    class Meta(object):
        db_table = 'schemas_season'
    #def __str__(self):
    #return self.number
    #def __int__(self):
    #return self.number


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('partOfSeries', 'number')


class Episode(models.Model):
    #episodes in a tv series have a list of episode objects
    episodeNumber = models.IntegerField(null=True, blank=True, default=None)
    partOfSeason = models.ForeignKey(Season, null=True, blank=True, default=None)
    partOfSeries = models.ForeignKey(TVSeries, null=True, blank=True, default=None)
    #kukepisode = models.OneToOneField(KukEpisode, null=True, blank=True, default = None)
    new_episode = models.OneToOneField(NewEpisode, null=True, blank=True, default=None)
    name = models.TextField()
    interactionCount = models.CharField(max_length=200, default='', blank=True)
    subtitle_rating = models.IntegerField(null=True, blank=True, default=None)
    views = models.ManyToManyField(View, null=True, blank=True, default=None,db_table='schemas_episode_views')

    class Meta(object):
        db_table = 'schemas_episode'
    #def __str__(self):
    #return str(self.partOfSeason.number) + ',' + str(self.episodeNumber)


class TVSeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name',)


country_dict = {"AF": "Afgh\u00e1nist\u00e1n", "AX": "Alandy", "AL": "Alb\u00e1nie", "DZ": "Al\u017e\u00edrsko",
                "AS": "Americk\u00e1 Samoa", "VI": "Americk\u00e9 Panensk\u00e9 ostrovy", "AD": "Andorra",
                "AO": "Angola", "AI": "Anguila", "AQ": "Antarktida", "AG": "Antigua a Barbuda", "AR": "Argentina",
                "AM": "Arm\u00e9nie", "AW": "Aruba", "AU": "Austr\u00e1lie", "BS": "Bahamy", "BH": "Bahrajn",
                "BD": "Banglad\u00e9\u0161", "BB": "Barbados", "BE": "Belgie", "BZ": "Belize", "BJ": "Benin",
                "BM": "Bermudy", "BT": "Bh\u00fat\u00e1n", "BO": "Bol\u00edvie", "BA": "Bosna a Hercegovina",
                "BW": "Botswana", "BR": "Braz\u00edlie", "VG": "Britsk\u00e9 Panensk\u00e9 ostrovy",
                "IO": "Britsk\u00e9 \u00fazem\u00ed v Indick\u00e9m oce\u00e1nu", "BN": "Brunej Darussalam",
                "BG": "Bulharsko", "BF": "Burkina Faso", "BI": "Burundi", "BY": "B\u011blorusko", "CL": "Chile",
                "HR": "Chorvatsko", "CK": "Cookovy ostrovy", "CD": "Demokratick\u00e1 republika Kongo",
                "DM": "Dominika", "DO": "Dominik\u00e1nsk\u00e1 republika", "DK": "D\u00e1nsko", "DJ": "D\u017eibuti",
                "EG": "Egypt", "EC": "Ekv\u00e1dor", "SV": "El Salvador", "ER": "Eritrea", "EE": "Estonsko",
                "ET": "Etiopie", "FO": "Faersk\u00e9 ostrovy", "FK": "Falklandsk\u00e9 ostrovy", "FJ": "Fid\u017ei",
                "PH": "Filip\u00edny", "FI": "Finsko", "FR": "Francie", "GF": "Francouzsk\u00e1 Guyana",
                "PF": "Francouzsk\u00e1 Polyn\u00e9sie", "TF": "Francouzsk\u00e1 ji\u017en\u00ed teritoria",
                "GA": "Gabon", "GM": "Gambie", "GH": "Ghana", "GI": "Gibraltar", "GD": "Grenada", "GE": "Gruzie",
                "GL": "Gr\u00f3nsko", "GP": "Guadeloupe", "GU": "Guam", "GT": "Guatemala", "GG": "Guernsey",
                "GN": "Guinea", "GW": "Guinea-Bissau", "GY": "Guyana", "HT": "Haiti", "HN": "Honduras",
                "HK": "Hongkong, zvl\u00e1\u0161tn\u00ed administrativn\u00ed oblast \u010c\u00edny", "IN": "Indie",
                "ID": "Indon\u00e9sie", "IE": "Irsko", "IQ": "Ir\u00e1k", "IS": "Island", "IT": "It\u00e1lie",
                "IL": "Izrael", "JM": "Jamajka", "JP": "Japonsko", "YE": "Jemen", "JE": "Jersey",
                "ZA": "Jihoafrick\u00e1 republika",
                "GS": "Ji\u017en\u00ed Georgie a Ji\u017en\u00ed Sandwichovy ostrovy", "KR": "Ji\u017en\u00ed Korea",
                "JO": "Jord\u00e1nsko", "KY": "Kajmansk\u00e9 ostrovy", "KH": "Kambod\u017ea", "CM": "Kamerun",
                "CA": "Kanada", "CV": "Kapverdy", "QA": "Katar", "KZ": "Kazachst\u00e1n", "KE": "Ke\u0148a",
                "KI": "Kiribati", "CC": "Kokosov\u00e9 ostrovy", "CO": "Kolumbie", "KM": "Komory", "CG": "Kongo",
                "CR": "Kostarika", "CU": "Kuba", "KW": "Kuvajt", "CY": "Kypr", "KG": "Kyrgyzst\u00e1n", "LS": "Lesotho",
                "LB": "Libanon", "LY": "Libye", "LR": "Lib\u00e9rie", "LI": "Lichten\u0161tejnsko",
                "LA": "Lidov\u011b demokratick\u00e1 republika Laos", "LT": "Litva", "LV": "Loty\u0161sko",
                "LU": "Lucembursko", "MK": "Macedonia", "MG": "Madagaskar", "MV": "Maladivy", "MY": "Malajsie",
                "MW": "Malawi", "ML": "Mali", "MT": "Malta", "MA": "Maroko", "MH": "Marshallovy ostrovy",
                "MQ": "Martinik", "MU": "Mauricius", "MR": "Maurit\u00e1nie", "YT": "Mayotte", "HU": "Ma\u010farsko",
                "UM": "Men\u0161\u00ed odlehl\u00e9 ostrovy USA", "MX": "Mexiko", "FM": "Mikron\u00e9zie",
                "MD": "Moldavsko, republika", "MC": "Monako", "MN": "Mongolsko", "MS": "Montserrat", "MZ": "Mosambik",
                "MM": "Myanmar", "NA": "Namibie", "NR": "Nauru", "NP": "Nep\u00e1l",
                "ZZ": "Nezn\u00e1m\u00e1 nebo neplatn\u00e1 oblast", "NE": "Niger", "NG": "Nig\u00e9rie",
                "NI": "Nikaragua", "NU": "Niue", "NL": "Nizozemsko", "AN": "Nizozemsk\u00e9 Antily", "NF": "Norfolk",
                "NO": "Norsko", "NC": "Nov\u00e1 Kaledonie", "NZ": "Nov\u00fd Z\u00e9land", "DE": "N\u011bmecko",
                "OM": "Om\u00e1n", "BV": "Ostrov Bouvet", "IM": "Ostrov Man", "TC": "Ostrovy Caicos a Turks",
                "HM": "Ostrovy Heard a McDonald", "PW": "Palau", "PS": "Palestinian Territory", "PA": "Panama",
                "PG": "Papua-Nov\u00e1 Guinea", "PY": "Paraguay", "PE": "Peru", "PN": "Pitcairn",
                "CI": "Pob\u0159e\u017e\u00ed slonoviny", "PL": "Polsko", "PR": "Portoriko", "PT": "Portugalsko",
                "PK": "P\u00e1kist\u00e1n", "AT": "Rakousko", "GQ": "Rovn\u00edkov\u00e1 Guinea", "RO": "Rumunsko",
                "RU": "Rusko", "RW": "Rwanda", "RE": "R\u00e9union", "WS": "Samoa", "SM": "San Marino",
                "SA": "Sa\u00fadsk\u00e1 Ar\u00e1bie", "SN": "Senegal", "KP": "Severn\u00ed Korea",
                "MP": "Severn\u00ed Mariany", "SC": "Seychely", "SL": "Sierra Leone", "SG": "Singapur",
                "SK": "Slovensko", "SI": "Slovinsko", "SO": "Som\u00e1lsko",
                "AE": "Spojen\u00e9 arabsk\u00e9 emir\u00e1ty", "US": "Spojen\u00e9 st\u00e1ty", "RS": "Srbsko",
                "CS": "Srbsko a \u010cern\u00e1 Hora", "LK": "Sr\u00ed Lanka",
                "CF": "St\u0159edoafrick\u00e1 republika", "SR": "Surinam", "SJ": "Svalbard a Jan Mayen",
                "SH": "Svat\u00e1 Helena", "LC": "Svat\u00e1 Lucie", "BL": "Svat\u00fd Bartolom\u011bj",
                "KN": "Svat\u00fd Kitts a Nevis", "MF": "Svat\u00fd Martin", "PM": "Svat\u00fd Pierre a Miquelon",
                "ST": "Svat\u00fd Tom\u00e1\u0161", "VC": "Svat\u00fd Vincent a Grenadiny", "VA": "Svat\u00fd stolec",
                "SZ": "Svazijsko", "SD": "S\u00fad\u00e1n", "SY": "S\u00fdrie", "TZ": "Tanzanie", "TW": "Tchaj-wan",
                "TH": "Thajsko", "TG": "Togo", "TK": "Tokelau", "TO": "Tonga", "TT": "Trinidad a Tobago",
                "TN": "Tunisko", "TR": "Turecko", "TM": "Turkmenist\u00e1n", "TV": "Tuvalu",
                "TJ": "T\u00e1d\u017eikist\u00e1n", "UG": "Uganda", "UA": "Ukrajina", "UY": "Uruguay",
                "UZ": "Uzbekist\u00e1n", "VU": "Vanuatu", "GB": "Velk\u00e1 Brit\u00e1nie", "VE": "Venezuela",
                "VN": "Vietnam", "CX": "V\u00e1no\u010dn\u00ed ostrovy", "TL": "V\u00fdchodn\u00ed Timor",
                "WF": "Wallis a Futuna", "ZM": "Zambie", "ZW": "Zimbabwe",
                "MO": "Zvl\u00e1\u0161tn\u00ed administrativn\u00ed oblast \u010c\u00edny Macao",
                "EH": "Z\u00e1padn\u00ed Sahara", "AZ": "\u00c1zerb\u00e1jd\u017e\u00e1n", "IR": "\u00cdr\u00e1n",
                "TD": "\u010cad", "ME": "\u010cern\u00e1 Hora", "CZ": "\u010cesk\u00e1 republika",
                "CN": "\u010c\u00edna", "GR": "\u0158ecko", "SB": "\u0160alamounovy ostrovy",
                "ES": "\u0160pan\u011blsko", "SE": "\u0160v\u00e9dsko", "CH": "\u0160v\u00fdcarsko"}













