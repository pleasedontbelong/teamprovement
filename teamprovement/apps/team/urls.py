from django.conf.urls import url
from django.urls import path

from team import views

urlpatterns = [
    path('', views.TeamView.as_view(), name='team'),
]
