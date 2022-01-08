from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.takedata,name='takedata'),
    path('resultfile',views.resultfile,name='resultfile')
]
