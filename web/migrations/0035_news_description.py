# Generated by Django 4.1.3 on 2023-02-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=0, max_length=1000, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
