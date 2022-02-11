# Generated by Django 3.2.9 on 2021-12-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0149_invite_key_required_default_expiry_backfill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisecustomerinvitekey',
            name='expiration_date',
            field=models.DateTimeField(help_text='The key will no longer be valid after this date.'),
        ),
        migrations.AlterField(
            model_name='historicalenterprisecustomerinvitekey',
            name='expiration_date',
            field=models.DateTimeField(help_text='The key will no longer be valid after this date.'),
        ),
    ]