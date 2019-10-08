from braces.views import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, DeleteView,
                                  UpdateView)
from django.urls import reverse_lazy
from .models import Meeting


class MeetingCRUD(LoginRequiredMixin):
    model = Meeting


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
