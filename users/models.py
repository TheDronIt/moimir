from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    account_type_list = [
        ("Пользователь", "Пользователь"),
        ("Детский", "Детский"),
        ("Работодатель", "Работодатель")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    name = models.CharField(verbose_name="Имя", max_length=50, null=True, blank=True)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, null=True, blank=True)
    age =  models.IntegerField(verbose_name="Возраст", null=True, blank=True)
    bio =  models.TextField(verbose_name="О себе", blank=True)
    account_type = models.CharField(max_length=50, choices=account_type_list, default="Пользователь", verbose_name="Тип аккаунта")
    employer = models.CharField(verbose_name="Название организации", max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username

    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    