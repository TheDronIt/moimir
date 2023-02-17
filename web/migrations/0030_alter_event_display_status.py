# Generated by Django 4.1.3 on 2023-02-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_event_display_status_alter_event_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='display_status',
            field=models.CharField(choices=[('Отображать', 'Отображать'), ('Скрывать', 'Скрывать')], default='Скрывать', max_length=50, verbose_name='Статус отображения'),
        ),
    ]
