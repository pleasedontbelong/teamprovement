# Generated by Django 2.2.6 on 2019-10-09 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_topic_meeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='meeting.Meeting'),
        ),
    ]