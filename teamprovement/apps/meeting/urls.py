from django.conf.urls import url
from django.urls import path

from meeting import views

urlpatterns = [
    url(r'^$', views.MeetingListView.as_view(), name='meeting_list'),
    path('<int:pk>', views.MeetingDetailView.as_view(), name='meeting_detail'),
    path('add', views.MeetingCreateView.as_view(), name='meeting_create'),
    path('delete/<int:pk>', views.MeetingDeleteView.as_view(), name='meeting_delete'),
    path('join/<int:pk>', views.MeetingJoinView.as_view(), name='meeting_join'),
    path('update/<int:pk>', views.MeetingUpdateView.as_view(), name='meeting_update'),
    path('<int:meeting_id>/topic/add', views.TopicCreateView.as_view(), name='topic_create'),
    path('<int:meeting_id>/topic/<int:pk>/update', views.TopicUpdateView.as_view(), name='topic_update'),
    path(
        '<int:meeting_id>/topic/<int:topic_id>/action/add',
        views.ActionCreateView.as_view(),
        name='action_create'
    ),
    path(
        '<int:meeting_id>/action/<int:pk>/update',
        views.ActionUpdateView.as_view(),
        name='action_update'
    ),
    path(
        '<int:meeting_id>/topic/<int:topic_id>/comment/add',
        views.CommentCreateView.as_view(),
        name='comment_create'
    ),
    path(
        '<int:meeting_id>/topic/<int:topic_id>/comment/<int:pk>/update',
        views.CommentUpdateView.as_view(),
        name='comment_update'
    ),
    path(
        '<int:meeting_id>/topic/<int:topic_id>/comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(),
        name='comment_delete'
    ),
]
