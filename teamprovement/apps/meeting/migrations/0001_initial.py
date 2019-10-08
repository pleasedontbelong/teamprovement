# Generated by Django 2.2.6 on 2019-10-08 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('was_successful', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.PositiveSmallIntegerField(choices=[(2, 'Good'), (1, 'Neutral'), (0, 'Bad')])),
                ('fact', models.CharField(max_length=255)),
                ('feeling', models.TextField()),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.Action')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.PositiveSmallIntegerField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Participant')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.User'),
        ),
        migrations.AddField(
            model_name='participant',
            name='votes',
            field=models.ManyToManyField(through='meeting.Vote', to='meeting.Topic'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Participant')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Meeting'),
        ),
        migrations.AddField(
            model_name='action',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Participant'),
        ),
    ]
