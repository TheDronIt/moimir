# Generated by Django 4.0.6 on 2023-02-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_2.png', upload_to='profile_pics'),
        ),
    ]