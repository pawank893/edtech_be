# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('is_choice_correct', models.BooleanField(default=False)),
                ('choice', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('description', models.TextField()),
                ('diagram', models.CharField(max_length=500)),
                ('difficulty_level', models.IntegerField(default=1)),
                ('marks', models.FloatField()),
                ('hints', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionTestSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeriesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('series_type', models.CharField(choices=[(b'flash_test', b'flash_test'), (b'test_series', b'test_series'), (b'mock_test', b'mock_test')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100)),
                ('series_type', models.CharField(choices=[(b'flash_test', b'flash_test'), (b'test_series', b'test_series'), (b'mock_test', b'mock_test')], max_length=100)),
                ('is_paid', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.Subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserQuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('is_correct', models.BooleanField(default=False)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='questiontestseries',
            name='test_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.TestSeries'),
        ),
        migrations.AddField(
            model_name='question',
            name='test_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edtech.TestSeries'),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.Topic'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech.Question'),
        ),
    ]
