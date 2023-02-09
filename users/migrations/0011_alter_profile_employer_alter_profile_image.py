# Generated by Django 4.1.3 on 2023-02-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_bio_alter_profile_employer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employer',
            field=models.CharField(blank=True, default='', max_length=50, null=True, unique=True, verbose_name='Название организации'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_4.png', upload_to='profile_pics'),
        ),
    ]