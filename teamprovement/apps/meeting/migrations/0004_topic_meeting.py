# Generated by Django 2.2.6 on 2019-10-09 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_auto_20191009_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='meeting',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='meeting.Meeting'),
            preserve_default=False,
        ),
    ]
