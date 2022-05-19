from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Major, Subject

Major_choices =  Major.objects.all().values_list('name', 'name')

class MajorModelForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ('name',)
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
        }

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('major', 'subject_name', 'prof_name', 'memo')
        widgets = {
            'major' : forms.Select(choices=Major_choices, attrs={'class': 'form-control'}),
            'subject_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Player Name'}),
            'prof_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Back Number'}),
            'memo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Preffered Foot'}),
        }
        