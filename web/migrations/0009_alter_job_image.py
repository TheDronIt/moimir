# Generated by Django 4.1.3 on 2023-02-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_job_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(default='default.png', upload_to='job_pics'),
        ),
    ]
