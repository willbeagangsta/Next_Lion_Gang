
from unicodedata import name
from django.contrib import admin
from django.urls import path
from subjectApp import views
from subjectApp.views import AddMajorView, AddSubjectView, EditSubjectView, EditMajorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addMajor', AddMajorView.as_view(), name="addMajor"),
    path('', views.home, name="home" ),
    path('addSubject', AddSubjectView.as_view(), name="addSubject"),
    path('computer', views.computerSubjectView, name="computer"),
    path('editSubject/<int:pk>', EditSubjectView.as_view(), name="editSubject"),
    path('deleteSubject/<int:subject_pk>', views.DeleteSubjectView, name="deleteSubject"),
    path('champions', views.championsSubjectView, name="champions"),
    path('editMajor/<int:pk>', EditMajorView.as_view(), name="editMajor"),
    path('deleteMajor/<int:major_pk>', views.DeleteMajorView, name="deleteMajor"),
    path('DeleteComplete', views.DeleteCompleteView  ,name="DeleteComplete"),
    path('MajorDetail/<int:major_pk>', views.majorDetailView, name="MajorDetail"),
]
