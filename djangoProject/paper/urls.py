from django.urls import path

from . import views

app_name = 'paper'

urlpatterns = [
    path('view/', views.view, name='view'),  # view one paper
    path('list/', views.index, name='index'),  # list all paper
    path('graph/', views.graph, name='graph'),  # graph on all paper
]
