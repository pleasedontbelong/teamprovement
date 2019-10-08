from django.conf.urls import url
from django.urls import path

from .views import MeetingListView, MeetingDetailView

urlpatterns = [
    url(r'^$', MeetingListView.as_view(), name='meeting_list'),
    path('<int:pk>', MeetingDetailView.as_view(), name='meeting_detail'),
]
