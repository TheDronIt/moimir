from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random
from PIL import Image
from web.models import *


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
    


class User_portfolio(models.Model):

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    type_of_employment_list = [
        ("Полная занятость", "Полная занятость"),
        ("Частичная занятость", "Частичная занятость"),
        ("Проектная работа", "Проектная работа"),
        ("Стажировка", "Стажировка")
    ]
    schedule_list = [
        ("Полный день", "Полный день"),
        ("Вахтовый метод", "Вахтовый метод"),
        ("Сменный график", "Сменный график"),
        ("Удаленная работа", "Удаленная работа"),
        ("Гибкий график", "Гибкий график"),
    ]
    special_conditions_list = [
        ("Проблемы со зрением", "Проблемы со зрением"),
        ("Проблемы со слухом", "Проблемы со слухом"),
        ("Проблемы c речью", "Проблемы c речью"),
        ("Нарушения опорно-двигательного аппарата", "Нарушения опорно-двигательного аппарата"),
        ("Ментальные нарушения", "Ментальные нарушения"),
        ("Другое", "Другое"),
        ("Отсутствуют", "Отсутствуют"),
    ]

    user =  models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="portfolio_user", null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    about = models.TextField(max_length=500, verbose_name="Ваше описание")
    work_experience = models.TextField(max_length=500, verbose_name="Опыт работы")
    education = models.TextField(max_length=500, verbose_name="Ваше описание")
    languages = models.TextField(max_length=500, verbose_name="Языки")
    link = models.CharField(verbose_name="Ссылка на портфолио", max_length=200, null=True, default=None)

    type_of_employment = models.CharField(verbose_name="Тип занятости", choices=type_of_employment_list, max_length=50)
    schedule = models.CharField(verbose_name="График работы", choices=schedule_list, max_length=50)
    special_conditions = models.CharField(verbose_name="Особые условия", choices=special_conditions_list, max_length=50)

    def __str__(self):
        return self.user.username


class Children_achievement(models.Model):
    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'

    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="achievements_user", null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    image = models.ImageField(verbose_name="Изображение", upload_to='achievements_pics')#default='default_achievement.png',
    about = models.TextField(max_length=500, verbose_name="Описание")
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.title}"

    '''
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''