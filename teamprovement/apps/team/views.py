from django.views.generic.base import TemplateView


class TeamView(TemplateView):
    template_name = "team/detail.jinja2"
