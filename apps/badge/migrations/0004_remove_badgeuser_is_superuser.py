# Generated by Django 4.2.7 on 2024-01-24 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0003_badgeuser_groups_badgeuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badgeuser',
            name='is_superuser',
        ),
    ]
