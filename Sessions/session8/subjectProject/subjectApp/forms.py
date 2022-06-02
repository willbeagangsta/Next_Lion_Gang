from socket import fromshare
from django import forms
from .models import Major, Subject

Major_choices = Major.objects.all().values_list('title', 'title')

class MajorModelForm(forms.ModelForm):
    class Meta:
        model = Major
        fields =  ('title',)
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전공을 입력하세요.'}),
        }

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = {'major', 'professor', 'name', 'Memo'}
        widgets = {
            'major' : forms.Select(choices=Major_choices, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '과목명을 입력하세요.'}),
            'professor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '교수님 이름을 입력하세요.'}),
            'Memo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '메모 사항을 입력하세요.'}),

        }