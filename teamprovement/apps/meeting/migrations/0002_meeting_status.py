# Generated by Django 2.2.6 on 2019-10-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Opened'), (1, 'Closed')], default=1),
            preserve_default=False,
        ),
    ]
