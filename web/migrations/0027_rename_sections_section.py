# Generated by Django 4.1.3 on 2023-02-17 07:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0026_sections'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sections',
            new_name='Section',
        ),
    ]
