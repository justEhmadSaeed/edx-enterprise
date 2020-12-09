# Generated by Django 2.2.17 on 2020-12-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0116_auto_20201116_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_portal_lms_configurations_screen',
            field=models.BooleanField(default=False, help_text='Specifies whether to allow access to the external LMS configuration screen in the admin portal.'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_portal_lms_configurations_screen',
            field=models.BooleanField(default=False, help_text='Specifies whether to allow access to the external LMS configuration screen in the admin portal.'),
        ),
    ]
