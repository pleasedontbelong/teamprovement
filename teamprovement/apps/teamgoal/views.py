from braces.views import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, UpdateView)
from .models import TeamGoal
from django.urls import reverse_lazy


class TeamGoalCRUD(LoginRequiredMixin):
    model = TeamGoal
    success_url = reverse_lazy('meeting_list')


class TeamGoalCreateView(TeamGoalCRUD, CreateView):
    template_name = "teamgoal/create.jinja2"
    fields = ('title', 'actions')


class TeamGoalDeleteView(TeamGoalCRUD, DeleteView):
    template_name = "teamgoal/delete.jinja2"


class TeamGoalUpdateView(TeamGoalCRUD, UpdateView):
    template_name = "teamgoal/update.jinja2"
    fields = ('title', 'actions')
