# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 11:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardedPointValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_object_id', models.IntegerField(null=True)),
                ('reason', models.CharField(max_length=140)),
                ('points', models.IntegerField()),
                ('source_object_id', models.IntegerField(null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('source_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awardedpointvalue_sources', to='contenttypes.ContentType')),
                ('source_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awardedpointvalue_sources', to=settings.AUTH_USER_MODEL)),
                ('target_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awardedpointvalue_targets', to='contenttypes.ContentType')),
                ('target_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awardedpointvalue_targets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PointValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TargetStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_object_id', models.IntegerField(null=True)),
                ('points', models.IntegerField(default=0)),
                ('position', models.PositiveIntegerField(null=True)),
                ('level', models.PositiveIntegerField(default=1)),
                ('target_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='targetstat_targets', to='contenttypes.ContentType')),
                ('target_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='targetstat_targets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='awardedpointvalue',
            name='value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_points.PointValue'),
        ),
        migrations.AlterUniqueTogether(
            name='targetstat',
            unique_together=set([('target_content_type', 'target_object_id')]),
        ),
    ]
