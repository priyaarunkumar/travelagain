from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.fun,name='fun'),
    path('regi' ,views.regi, name='regi'),
    # path('search/', views.search,name='search'),
]
