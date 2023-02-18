from django.db import models
from django.contrib.auth.models import User
import random
from PIL import Image


class Profile(models.Model):
    account_type_list = [
        ("Пользователь", "Пользователь"),
        ("Детский", "Детский"),
        ("Работодатель", "Работодатель")
    ]
    show_list = [
        ("Отображать", "Отображать"),
        ("Скрывать", "Скрывать")
    ]

    def random_default_image():
        image_list = [
            'default_1.png',
            'default_2.png',
            'default_3.png',
            'default_4.png',
        ]

        image = random.choice(image_list)
        return image

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default=random_default_image(), upload_to='profile_pics')
    name = models.CharField(verbose_name="Имя", max_length=50, null=True, blank=True)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, null=True, blank=True)
    age =  models.IntegerField(verbose_name="Возраст", null=True, blank=True)
    bio =  models.TextField(max_length=500, verbose_name="О себе", blank=True)
    contacts = models.CharField(verbose_name="Контакты", max_length=50, null=True, blank=True)
    show_email = models.CharField(max_length=50, choices=show_list, default="Скрывать", verbose_name="Отображение почты")
    show_contacts = models.CharField(max_length=50, choices=show_list, default="Скрывать", verbose_name="Отображение контактов")
    account_type = models.CharField(max_length=50, choices=account_type_list, default="Пользователь", verbose_name="Тип аккаунта")
    employer = models.CharField(verbose_name="Название организации", max_length=50, default="", null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username

    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

