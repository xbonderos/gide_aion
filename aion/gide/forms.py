#coding=utf-8
from django import forms
from django.shortcuts import redirect
from ratings.models import Vote
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView


#class LikeForm(forms.Form):
#    pass

class LikeForm(forms.ModelForm):
    model = Vote
    template_name = 'testform.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        instance = form.save(commit=True)
        instance.save()
        #Vote.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())
