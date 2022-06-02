"""subjectProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from subjectApp import views
from subjectApp.views import AddMajorView, home, AddSubjectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addMajor', AddMajorView.as_view(), name="addMajor"),
    path('addSubject', AddSubjectView.as_view(), name="addSubject"),
    path('home', views.home, name="home"),
]
