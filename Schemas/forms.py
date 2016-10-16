# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from kukto.profiles.models import UserProfile

standard_library.install_hooks()
from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class RealActorForm(forms.ModelForm):
    class Meta:
        fields = ()


#name=models.CharField( blank=True, default = '', max_length=200)
#    birthDate = models.DateField(null=True, blank=True, default = None)
#    deathDate = models.DateField(null=True, blank=True, default = None)
#    duns = models.TextField( blank=True, default = '')
#    gender = models.CharField(max_length=100,  blank=True, default = '')
#    nationality = models.ForeignKey(Country, null=True, blank=True, default = None)
#    sameAs = models.URLField(null=True, blank=True, default = None)
#    images = models.TextField(null=True, blank=True, default = None)


class PersonForm(forms.ModelForm):
    class Meta:
        fields = (
            ''
        )


class PersonsForm(forms.Form):
    birthDate = forms.DateField(required=False, )
    deathDate = forms.DateField(required=False)
    duns = forms.CharField(required=False)
    gender = forms.CharField(max_length=100, required=False)
    nationality = forms.CharField(max_length=200, required=False)
    sameAs = forms.URLField(required=False)
    images = forms.ImageField(required=False)

