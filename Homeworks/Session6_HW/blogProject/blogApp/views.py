from contextlib import redirect_stderr
from sqlite3 import ProgrammingError
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.




def new(request):
    if request.method == 'POST':
        # POST 요청으로 온 데이터 확인
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']

        )
        return redirect('list')
    
    return render(request, 'new.html')

def list(request):
    article = Article.objects.all()
    return render(request, 'list.html', {'article': article})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def hobby(request):
    article = Article.objects.get(category=hobby)
    return render(request, 'hobby.html', {'category':hobby})
    
def food(request):
    article = Article.objects.get(category=food)
    return render(request, 'food.html', {'category':food})

def programming(request):
    article = Article.objects.get(category=programming)
    return render(request, 'programming.html', {'category':programming})