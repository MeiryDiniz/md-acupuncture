# Generated by Django 5.0.6 on 2024-11-29 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='eircode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street',
        ),
    ]