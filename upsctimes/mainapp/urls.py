from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('readArticle/<str:slug>', views.readArticle, name = 'readArticle'),
    # path('booksSection/', views.getbooks,name = "getbooks"),
    path('questionpapers/', views.questionpapers,name = "questionpapers"),
    path('notes/', views.notes,name = "notes"),
    path('quiz/', views.quiz,name = "quiz"),
    path('jobs/', views.jobs,name = "jobs"),
    path('corporatejobs/', views.corporatejobs,name = "corporatejobs"),
    path('email/', views.email, name = "email"),
    path('polity/', views.Polity,name = "polity"),
    path('generalscience/', views.Generalscience,name = "generalscience"),
    path('currentaffairs/', views.Currentaffairs,name = "currentaffairs"),
    path('geography/',views.Geography, name = "geography"),
    path('searchh/', views.searchh, name = "searchh"),
    path('searchg/', views.searchg, name = "searchg"),
    path('searchp/', views.searchp, name = "searchp"),
    path('searchgs/', views.searchgs, name = "searchgs"),
    path('searchca/', views.searchca, name = "searchca"),
    path('searchblog/', views.searchblog, name = "searchblog"),
    path('searchnotes/', views.searchnotes, name = "searchnotes"),
    path('searchpapers/', views.searchpapers, name = "searchpapers"),
    path('searchjobs/', views.searchjobs, name = "searchjobs"),
    path('readgjob/<str:slug>', views.readgjob, name = "readgjob"),
]