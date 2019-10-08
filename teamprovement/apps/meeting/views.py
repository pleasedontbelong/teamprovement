from django.views.generic import ListView, TemplateView
from .models import Meeting


# class MeetingListView(ListView):
#     model = Meeting
#     template_name = "meeting/list.jinja2"

class MeetingListView(TemplateView):
    template_name = "meeting/list.jinja2"
