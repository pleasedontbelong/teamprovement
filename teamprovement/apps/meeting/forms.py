from django import forms

from meeting.models import Topic, Action, Participant, Comment


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


class ActionCreateForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('goal', 'description', 'owner')

    def __init__(self, *args, **kwargs):
        self.meeting = kwargs.pop('meeting')
        self.topic = kwargs.pop('topic')
        super().__init__(*args, **kwargs)
        self.fields['owner'].queryset = Participant.objects.filter(
            meeting=self.meeting
        )

    def save(self, **kwargs):
        self.instance.meeting = self.meeting
        self.instance.save()
        self.topic.action = self.instance
        self.topic.save()
        return self.instance


class ActionUpdateForm(ActionCreateForm):
    class Meta:
        model = Action
        fields = ('goal', 'description', 'owner', 'was_successful')

    def save(self, **kwargs):
        self.instance.save()
        return self.instance


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        self.topic = kwargs.pop('topic')
        self.author = kwargs.pop('author')
        super().__init__(*args, **kwargs)

    def save(self, **kwargs): 
        self.instance.topic = self.topic
        self.instance.author = self.author
        self.instance.save()
        return self.instance      
      
        
