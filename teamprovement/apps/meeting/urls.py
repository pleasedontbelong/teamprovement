from django.conf.urls import url
from django.urls import path

from .views import (MeetingListView, MeetingDetailView, MeetingCreateView,
                    MeetingDeleteView, MeetingUpdateView, TopicCreateView)

urlpatterns = [
    url(r'^$', MeetingListView.as_view(), name='meeting_list'),
    path('<int:pk>', MeetingDetailView.as_view(), name='meeting_detail'),
    path('add', MeetingCreateView.as_view(), name='meeting_create'),
    path('delete/<int:pk>', MeetingDeleteView.as_view(), name='meeting_delete'),
    path('update/<int:pk>', MeetingUpdateView.as_view(), name='meeting_update'),
    path('<int:meeting_id>/topic/add', TopicCreateView.as_view(), name='topic_create'),
]
