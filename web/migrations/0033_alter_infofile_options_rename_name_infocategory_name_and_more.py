# Generated by Django 4.1.3 on 2023-02-18 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_infocategory_infofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infofile',
            options={'verbose_name': 'Полезная информация', 'verbose_name_plural': 'Полезная информация'},
        ),
        migrations.RenameField(
            model_name='infocategory',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='infofile',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='infofile',
            old_name='File',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='infofile',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='infofile',
            old_name='Visibility',
            new_name='visibility',
        ),
    ]