# Generated by Django 4.1.3 on 2023-02-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_remove_user_portfolio_experience_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_4.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='user_portfolio',
            name='link',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='Ссылка на портфолио'),
        ),
    ]