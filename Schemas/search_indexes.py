from haystack import indexes
from kukto.Schemas.models import TVSeries, Movie


class TVSeriesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return TVSeries

    def index_queryset(self, using=None):
        return TVSeries.objects.all()


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Movie

    def index_queryset(self, using=None):
        return Movie.objects.all()
