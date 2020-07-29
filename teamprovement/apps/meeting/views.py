from braces.views import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, DeleteView,
                                  UpdateView, RedirectView)
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .forms import TopicForm, ActionCreateForm, ActionUpdateForm, CommentCreateForm
from .models import Meeting, Topic, Action, Comment, Participant, Vote
from .exceptions import MaxVotesPerParticipantException


class MeetingCRUD(LoginRequiredMixin):
    model = Meeting


class TopicCRUD(LoginRequiredMixin):
    model = Topic

    def dispatch(self, request, *args, **kwargs):
        self.meeting = Meeting.objects.get(pk=kwargs['meeting_id'])
        return super().dispatch(request, *args, **kwargs)


class CommentCRUD(LoginRequiredMixin):
    model = Comment

    def dispatch(self, request, *args, **kwargs):
        self.meeting = Meeting.objects.get(pk=kwargs['meeting_id'])
        return super().dispatch(request, *args, **kwargs)


class ActionCRUD(LoginRequiredMixin):
    model = Action

    def dispatch(self, request, *args, **kwargs):
        self.meeting = Meeting.objects.get(pk=kwargs['meeting_id'])
        return super().dispatch(request, *args, **kwargs)


class ParticipantAccessMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self, user):
        return Participant.objects.filter(user=user, meeting_id=self.kwargs['pk']).exists()


class MeetingListView(MeetingCRUD, ListView):
    template_name = "meeting/list.jinja2"
    context_object_name = "meetings"
    ordering = ("-created_at")


class MeetingDetailView(MeetingCRUD, ParticipantAccessMixin, DetailView):
    template_name = "meeting/detail.jinja2"


class MeetingCreateView(MeetingCRUD, CreateView):
    template_name = "meeting/create.jinja2"
    fields = ('name',)
    success_url = reverse_lazy('meeting_list')

    def form_valid(self, form):
        redirect = super().form_valid(form)
        # Add the creator to the participants
        self.object.add(self.request.user)
        return redirect


class MeetingDeleteView(MeetingCRUD, ParticipantAccessMixin, DeleteView):
    template_name = "meeting/delete.jinja2"
    success_url = reverse_lazy('meeting_list')


class MeetingUpdateView(MeetingCRUD, ParticipantAccessMixin, UpdateView):
    template_name = "meeting/update.jinja2"
    success_url = reverse_lazy('meeting_list')
    fields = ('name', 'status')
    context_object_name = "meeting"


class MeetingJoinView(MeetingCRUD, RedirectView):
    permanent = False
    url = reverse_lazy('meeting_list')

    def get(self, *args, **kwargs):
        meeting = get_object_or_404(Meeting, pk=kwargs['pk'])
        if not meeting.is_participant(self.request.user):
            meeting.add(self.request.user)
        return super().get(*args, **kwargs)


class TopicCreateView(TopicCRUD, CreateView):
    template_name = "topic/create.jinja2"
    form_class = TopicForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['meeting'] = self.meeting
        return context

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.meeting.id])

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['creator'] = self.meeting.participants.get(user=self.request.user)
        form_kwargs['meeting'] = self.meeting
        return form_kwargs


class TopicUpdateView(TopicCRUD, UpdateView):
    template_name = "topic/update.jinja2"
    form_class = TopicForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['meeting'] = self.meeting
        return context

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.meeting.id])

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['creator'] = self.meeting.participants.get(user=self.request.user)
        form_kwargs['meeting'] = self.meeting
        return form_kwargs


class ActionCreateView(ActionCRUD, CreateView):
    model = Action
    template_name = "action/create.jinja2"
    form_class = ActionCreateForm

    def dispatch(self, request, *args, **kwargs):
        self.topic = Topic.objects.get(
            pk=kwargs['topic_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['meeting'] = self.meeting
        context['topic'] = self.topic
        return context

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['topic'] = self.topic
        form_kwargs['meeting'] = self.meeting
        return form_kwargs

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.meeting.id])


class ActionUpdateView(ActionCRUD, UpdateView):
    model = Action
    template_name = "action/update.jinja2"
    form_class = ActionUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['topics'] = Topic.objects.filter(action=self.object)
        return context

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.object.meeting.id])

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['topic'] = None
        form_kwargs['meeting'] = self.meeting
        return form_kwargs


class CommentCreateView(CommentCRUD, CreateView):
    model = Comment
    template_name = "comment/create.jinja2"
    form_class = CommentCreateForm

    def dispatch(self, request, *args, **kwargs):
        self.topic = Topic.objects.get(
            pk=kwargs['topic_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['meeting'] = self.meeting
        context['topic'] = self.topic
        return context

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['topic'] = self.topic
        form_kwargs['author'] = self.meeting.participants.get(user=self.request.user)
        return form_kwargs

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.meeting.id])


class VoteTopicView(CreateView):
    model = Vote
    fields = ('topic', 'participant')

    def dispatch(self, request, *args, **kwargs):
        self.meeting = Meeting.objects.get(pk=kwargs['meeting_id'])
        try:
            return super().dispatch(request, *args, **kwargs)
        except MaxVotesPerParticipantException:
            messages.error(self.request, "Max votes reached")
            return redirect(reverse('meeting_detail', args=[self.meeting.id]))

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': {
                    'topic': self.kwargs['topic_id'],
                    'participant': self.meeting.participants.get(
                        user=self.request.user
                    ).pk
                }
            })
        return kwargs

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.meeting.id])


class UnvoteTopicView(DeleteView):
    model = Vote

    def dispatch(self, request, *args, **kwargs):
        self.meeting = Meeting.objects.get(pk=kwargs['meeting_id'])
        self.topic = Topic.objects.get(pk=kwargs['topic_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, *args, **kwargs):
        return Vote.objects.filter(
            topic=self.topic,
            participant=self.meeting.participants.get(user=self.request.user)
        ).first()

    def get_success_url(self):
        return reverse('meeting_detail', args=[self.meeting.id])
