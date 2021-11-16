from django.urls import path

from . import views

app_name = 'information'

urlpatterns = [
    path('getPaper/', views.get_paper_from_api, name='getPaper'),
    path('generateNewPapers/', views.generate_new_papers, name='generateNewPapers'),
]
