# Generated by Django 4.1.3 on 2023-02-17 08:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0027_rename_sections_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='section',
            name='event_location',
        ),
        migrations.RemoveField(
            model_name='section',
            name='event_time',
        ),
        migrations.AddField(
            model_name='section',
            name='age_limit',
            field=models.CharField(choices=[('Для детей', 'Для детей'), ('Для взрослых', 'Для взрослых'), ('Без ограничений', 'Без ограничений')], default=0, max_length=50, verbose_name='Возрастное ограничение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='event_theme',
            field=models.CharField(choices=[('Спорт', 'Спорт'), ('Волонтерство', 'Волонтерство'), ('Игры', 'Игры'), ('Театральное искусство', 'Театральное искусство'), ('Образование', 'Образование'), ('Творчество', 'Творчество'), ('Другое', 'Другое')], max_length=50, verbose_name='Тема секции'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название услуги волонтера')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('date', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Дата')),
                ('event_location', models.CharField(max_length=50, verbose_name='Адрес мероприятия')),
                ('event_date', models.DateField(verbose_name='Дата мероприятия')),
                ('event_time', models.TimeField(verbose_name='Время мероприятия')),
                ('event_theme', models.CharField(choices=[('Спорт', 'Спорт'), ('Цирк', 'Цирк'), ('Городские события', 'Городские события'), ('Игры и квесты', 'Игры и квесты'), ('Театры', 'Театры'), ('Концерты', 'Концерты'), ('Музеи и галереи', 'Музеи и галереи'), ('Экскурсии ', 'Экскурсии '), ('Обучение ', 'Обучение '), ('Творчество', 'Творчество')], max_length=50, verbose_name='Тема мероприятия')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Мероприятия',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]