# Generated by Django 4.1.3 on 2023-02-08 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_employer'),
        ('web', '0012_alter_job_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Аккаунт организации'),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='job_pics'),
        ),
    ]
