from django.conf.urls import url
from django.urls import path

from teamgoal import views

urlpatterns = [
    path('', views.TeamGoalListView.as_view(), name='teamgoal_list'),
    path('add', views.TeamGoalCreateView.as_view(), name='teamgoal_create'),
    path('delete/<int:pk>', views.TeamGoalDeleteView.as_view(), name='teamgoal_delete'),
    path('update/<int:pk>', views.TeamGoalUpdateView.as_view(), name='teamgoal_update'),
]
