# Generated by Django 4.1.3 on 2023-02-06 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_job_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_response',
            name='job_response',
        ),
        migrations.AddField(
            model_name='job_response',
            name='job',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='job_response', to='web.job'),
            preserve_default=False,
        ),
    ]
