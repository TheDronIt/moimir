# Generated by Django 4.1.3 on 2023-02-06 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_job_description_job_image_alter_job_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='web.job')),
                ('user', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вакансии (заявки)',
                'verbose_name_plural': 'Вакансии (Заявки)',
            },
        ),
    ]