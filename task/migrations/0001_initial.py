# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import task.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorDetail', models.TextField()),
                ('ca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='FbConnect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessToken', models.CharField(blank=True, max_length=150, null=True)),
                ('uid', models.CharField(blank=True, max_length=150, null=True)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MassNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass_message', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('ca', models.ManyToManyField(to='ca.CAProfile')),
                ('mark_read', models.ManyToManyField(blank=True, related_name='mark_read', to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to=task.models.get_user_image_folder)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBodyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentBodyDetail', models.TextField()),
                ('ca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskId', models.AutoField(primary_key=True, serialize=False)),
                ('taskName', models.CharField(max_length=50)),
                ('taskDescription', models.TextField()),
                ('deadLine', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(default=0)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('mark_read', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
    ]