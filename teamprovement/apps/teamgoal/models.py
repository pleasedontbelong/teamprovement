from django.db import models


class TeamGoal(models.Model):
    title = models.CharField(max_length=255)
    actions = models.ManyToManyField('meeting.Action', blank=True)

    def __str__(self):
        return self.title
