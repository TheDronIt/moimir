# Generated by Django 4.1.3 on 2023-02-09 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_remove_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_response',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Дата'),
        ),
    ]
