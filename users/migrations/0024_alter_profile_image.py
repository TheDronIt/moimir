# Generated by Django 4.1.3 on 2023-02-18 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_4.png', upload_to='profile_pics'),
        ),
    ]
