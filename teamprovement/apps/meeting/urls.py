from django.conf.urls import url
from .views import MeetingListView

urlpatterns = [
    url(r'^', MeetingListView.as_view(), name='meeting_list'),
]
