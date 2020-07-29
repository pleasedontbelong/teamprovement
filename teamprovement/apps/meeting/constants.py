from extended_choices import Choices

MOOD_CHOICES = Choices(
    ('GOOD', 2, 'Good'),
    ('NEUTRAL', 1, 'Neutral'),
    ('BAD', 0, 'Bad')
)

MEETING_STATUS_CHOICES = Choices(
    ('OPENED', 0, 'Opened'),
    ('CLOSED', 1, 'Closed')
)

MAX_VOTES_PER_MEETING = 5
