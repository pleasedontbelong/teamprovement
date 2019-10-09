from django import forms

from meeting.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('mood', 'fact', 'feeling')

    def __init__(self, *args, **kwargs):
        self.meeting = kwargs.pop('meeting')
        self.creator = kwargs.pop('creator')
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance.creator = self.creator
        self.instance.meeting = self.meeting
        self.instance.save()
        return self.instance
