from braces.views import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, DeleteView,
                                  UpdateView)
from django.urls import reverse_lazy, reverse

from teamprovement.apps.meeting.forms import TopicForm
from .models import Meeting, Topic


class MeetingCRUD(LoginRequiredMixin):
    model = Meeting


class TopicCRUD(LoginRequiredMixin):
    model = Topic

    def dispatch(self, request, *args, **kwargs):
        self.meeting = Meeting.objects.get(pk=kwargs['meeting_id'])
        return super().dispatch(request, *args, **kwargs)


class MeetingListView(MeetingCRUD, ListView):
    template_name = "meeting/list.jinja2"
    context_object_name = "meetings"
    ordering = "status"


class MeetingDetailView(MeetingCRUD, DetailView):
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


class MeetingDeleteView(MeetingCRUD, DeleteView):
    template_name = "meeting/delete.jinja2"
    success_url = reverse_lazy('meeting_list')


class MeetingUpdateView(MeetingCRUD, UpdateView):
    template_name = "meeting/update.jinja2"
    success_url = reverse_lazy('meeting_list')
    fields = ('name', 'status')
    context_object_name = "meeting"


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
