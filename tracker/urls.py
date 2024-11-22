from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team_list, name='team_list'),
    path('matches/', views.match_list, name='match_list'),
]
