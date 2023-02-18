# Generated by Django 4.1.3 on 2023-02-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_profile_account_type_alter_profile_contacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contacts',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_2.png', upload_to='profile_pics'),
        ),
    ]
