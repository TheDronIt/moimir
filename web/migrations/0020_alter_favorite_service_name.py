# Generated by Django 4.1.3 on 2023-02-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='service_name',
            field=models.CharField(choices=[('Специалисты', 'Специалисты'), ('Волонтерство', 'Волонтерство'), ('Нуждается в помощи', 'Нуждается в помощи'), ('Мероприятия', 'Мероприятия'), ('Секции', 'Секции')], max_length=50, verbose_name='Название услуги'),
        ),
    ]
