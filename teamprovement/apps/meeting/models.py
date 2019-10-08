from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from meeting.constants import MEETING_STATUS_CHOICES, MOOD_CHOICES


class Meeting(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=MEETING_STATUS_CHOICES,
        default=MEETING_STATUS_CHOICES.OPENED
    )

    def __str__(self):
        return self.name

    def is_participant(self, user):
        return self.participants.filter(user=user).exists()

    def add(self, user):
        return self.participants.create(user=user)

    @property
    def is_opened(self):
        return self.status == MEETING_STATUS_CHOICES.OPENED


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'username'


class Participant(models.Model):
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name="participants")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.ManyToManyField('Topic', through='Vote')


class Action(models.Model):
    goal = models.CharField(max_length=255)
    body = models.TextField()
    was_successful = models.BooleanField()
    owner = models.ForeignKey(Participant, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)


class Topic(models.Model):
    mood = models.PositiveSmallIntegerField(choices=MOOD_CHOICES)
    fact = models.CharField(max_length=255)
    feeling = models.TextField()
    creator = models.ForeignKey(Participant, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True)


class Comment(models.Model):
    author = models.ForeignKey(Participant, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField()


class Vote(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    mood = models.PositiveSmallIntegerField()
