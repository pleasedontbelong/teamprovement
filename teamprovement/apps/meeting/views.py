from django.views.generic import TemplateView, DetailView

from .models import Meeting


class MeetingListView(TemplateView):
    template_name = "meeting/list.jinja2"

    def get_context_data(self):
        return {'meetings': Meeting.objects.all()}


class MeetingDetailView(DetailView):
    template_name = "meeting/detail.jinja2"
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
