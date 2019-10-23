from braces.views import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, UpdateView, ListView)
from .models import TeamGoal
from django.urls import reverse_lazy


class TeamGoalCRUD(LoginRequiredMixin):
    model = TeamGoal
    success_url = reverse_lazy('meeting_list')


class TeamGoalListView(TeamGoalCRUD, ListView):
    template_name = "teamgoal/list.jinja2"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teamgoals'] = TeamGoal.objects.all()
        return context


class TeamGoalCreateView(TeamGoalCRUD, CreateView):
    template_name = "teamgoal/create.jinja2"
    fields = ('title', 'actions')


class TeamGoalDeleteView(TeamGoalCRUD, DeleteView):
    template_name = "teamgoal/delete.jinja2"


class TeamGoalUpdateView(TeamGoalCRUD, UpdateView):
    template_name = "teamgoal/update.jinja2"
    fields = ('title', 'actions')
