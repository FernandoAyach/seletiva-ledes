# Generated by Django 4.2.7 on 2024-01-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_usereditrequest_is_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereditrequest',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='usereditrequest',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usereditrequest',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usereditrequest',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
