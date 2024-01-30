# Generated by Django 3.2.23 on 2024-01-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0198_alter_enterprisecourseenrollment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_academies',
            field=models.BooleanField(default=False, help_text='If checked, the learners will be able to see the academies on the learner portal dashboard.', verbose_name='Display academies screen'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_academies',
            field=models.BooleanField(default=False, help_text='If checked, the learners will be able to see the academies on the learner portal dashboard.', verbose_name='Display academies screen'),
        ),
    ]
