from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from collections import defaultdict

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

    @property
    def topics_stats(self):
        groups = defaultdict(list)
        for topic in self.topics.all():
            groups[topic.mood].append(topic)
        return groups

    @property
    def has_actions(self):
        return self.actions.exists()


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

    def __str__(self):
        return self.user.username


class Action(models.Model):
    goal = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    was_successful = models.BooleanField(blank=True, null=True)
    owner = models.ForeignKey(Participant, on_delete=models.CASCADE, blank=True, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="actions")

    def __str__(self):
        return self.goal


class Topic(models.Model):
    mood = models.PositiveSmallIntegerField(choices=MOOD_CHOICES)
    fact = models.CharField(max_length=255)
    feeling = models.TextField()
    creator = models.ForeignKey(Participant, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True)
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name="topics"
    )

    def created_by(self, user):
        return self.creator.user == user


class Comment(models.Model):
    author = models.ForeignKey(Participant, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField()

    def is_author(self, user):
        return self.author.user == user

class Vote(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    mood = models.PositiveSmallIntegerField()
