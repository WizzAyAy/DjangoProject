from django.urls import path

from . import views

app_name = 'information'

urlpatterns = [
    # view one paper with the api route
    path('view/', views.view, name='view'),
    path('getPaper/', views.get_paper, name='view'),
]
