# Generated by Django 2.2.6 on 2019-10-09 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_meeting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Opened'), (1, 'Closed')], default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='meeting.Meeting'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]