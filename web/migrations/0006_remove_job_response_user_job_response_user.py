# Generated by Django 4.1.3 on 2023-02-06 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0005_remove_job_response_job_response_job_response_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_response',
            name='user',
        ),
        migrations.AddField(
            model_name='job_response',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_response_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
