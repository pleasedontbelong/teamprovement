# Generated by Django 2.2.6 on 2019-10-10 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0007_auto_20191009_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='meeting.Meeting'),
        ),
    ]