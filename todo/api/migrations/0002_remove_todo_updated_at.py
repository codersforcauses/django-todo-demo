# Generated by Django 4.0 on 2021-12-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
    ]
