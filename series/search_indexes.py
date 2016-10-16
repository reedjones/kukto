# -*- coding: utf-8 -*-
from haystack import indexes
from kukto.series.models import NewShow


class NewShowIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return NewShow

    def index_queryset(self, using=None):
        return NewShow.objects.all()


