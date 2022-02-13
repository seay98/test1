from multiprocessing.connection import Client
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('client', views.ClientView.as_view()),
    path('client/<curl>', views.ClientViewDetail.as_view()),
    path('poster', views.PosterView.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)