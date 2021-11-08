from django.urls import path

from . import views

app_name = 'paper'

urlpatterns = [
    # view one paper
    path('view/', views.view, name='view'),
    # list all paper
    path('list/', views.index, name='index'),
]
