# Generated by Django 5.1.1 on 2024-10-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='slug',
        ),
    ]
