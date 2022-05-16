from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Player, Team


Team_choices = Team.objects.all().values_list('name', 'name')

Foot_choices = (
    ('R', 'Right'),
    ('L', 'Left'),
    ('BOTH', 'Both'),
)
Position_choices = (
    ('FW', 'Forward'),
    ('MF', 'Midfielder'),
    ('DF', 'Defender'),
    ('GK', 'Goalkeeper')
)

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Team 
        fields= ('name', 'city', 'manager')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager'}),

        }

class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('position', 'player_name', 'team', 'nationality',
                  'preffered_foot', 'backnum')
        
        widgets = {
            'position' : forms.Select(choices=Position_choices, attrs={'class' : 'form-control'}),
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Player Name'}),
            'team': forms.Select(choices=Position_choices, attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'preffered_foot': forms.Select(choices=Foot_choices, attrs={'class': 'form-control'}),
            'backnum': forms.NumberInput(attrs={'class': 'form-control'})
        }
