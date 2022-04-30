from pyexpat import model
from django.shortcuts import render, redirect
from .models import  Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.
class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html' , {'majors': majors, 'subjects': subjects})

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__name = '컴퓨터학부')

    return render(request, 'computer.html', {'computerMajor': computerMajor})

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

def championsSubjectView(request):
    subjects = Subject.objects.all()
    championsMajor = subjects.filter(major__name = '챔스진출학과')

    return render(request, 'champions.html', {'championsMajor' : championsMajor})

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')

def DeleteMajorView(reqeust, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()

    return redirect('DeleteComplete')

def DeleteCompleteView(request):
    comment = '전공이 삭제 되었습니다.'

    return render(request, 'DeleteComplete.html', {'comment' : comment})

def majorDetailView(request, major_pk):
    TheMajor = Major.objects.get(pk=major_pk)
    subjects = Subject.objects.all()
    detailedMajor = subjects.filter(major__pk=major_pk)

    return render(request, 'MajorDetail.html', {'detailedMajor': detailedMajor, 'TheMajor': TheMajor})


