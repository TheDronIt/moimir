from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from datetime import datetime
from PIL import Image
from random import randrange

class Job(models.Model):

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'

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
    experience_list = [
        ("Не важно","Не важно"),
        ("До 1 года","До 1 года"),
        ("От 1 года","От 1 года"),
        ("От 2 лет","От 2 лет"),
        ("Более 5 лет","Более 5 лет"),
    ]
    special_conditions_list = [
        ("Проблемы со зрением", "Проблемы со зрением"),
        ("Проблемы со слухом", "Проблемы со слухом"),
        ("Проблемы c речью", "Проблемы c речью"),
        ("Нарушения опорно-двигательного аппарата", "Нарушения опорно-двигательного аппарата"),
        ("Ментальные нарушения", "Ментальные нарушения"),
        ("Другое", "Другое"),
    ]

    title = models.CharField(verbose_name="Название вакансии", max_length=50)
    employer = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Аккаунт организации")
    min_salary = models.IntegerField(verbose_name="ЗП от")
    max_salary = models.IntegerField(verbose_name="ЗП до")
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)
    description = models.TextField(verbose_name="Описание")

    type_of_employment = models.CharField(verbose_name="Тип занятости", choices=type_of_employment_list, max_length=50)
    schedule = models.CharField(verbose_name="График работы", choices=schedule_list, max_length=50)
    experience = models.CharField(verbose_name="Опыт работы", choices=experience_list, max_length=50)
    special_conditions = models.CharField(verbose_name="Особые условия", choices=special_conditions_list, max_length=50)

    def __str__(self):
        return self.title



class Job_response(models.Model):
    class Meta:
        verbose_name = 'Вакансии (заявки)'
        verbose_name_plural = 'Вакансии (Заявки)'

    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="job_response_user", null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_response")
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.job.employer} ({self.job.title}): {self.user}"



class Favorite(models.Model):
    
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    service_name_list = [
        ("Специалисты", "Специалисты"),
        ("Волонтерство", "Волонтерство"),
        ("Нуждается в помощи", "Нуждается в помощи"),
        ("Мероприятия", "Мероприятия"),
        ("Секции", "Секции"),
    ]

    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="favorite_user", null=True)
    service_name = models.CharField(verbose_name="Название услуги", choices=service_name_list, max_length=50)
    service_id = models.IntegerField(verbose_name="ID услуги")

    def __str__(self):
        return f"{self.user}: {self.service_name} ({self.service_id})"



class Specialist(models.Model):

    class Meta:
        verbose_name = 'Специалисты'
        verbose_name_plural = 'Специалисты'

    experience_list = [
        ("До 1 года","До 1 года"),
        ("От 1 года","От 1 года"),
        ("От 2 лет","От 2 лет"),
        ("Более 5 лет","Более 5 лет"),
    ]
    special_conditions_list = [
        ("Проблемы со зрением", "Проблемы со зрением"),
        ("Проблемы со слухом", "Проблемы со слухом"),
        ("Проблемы c речью", "Проблемы c речью"),
        ("Нарушения опорно-двигательного аппарата", "Нарушения опорно-двигательного аппарата"),
        ("Ментальные нарушения", "Ментальные нарушения"),
        ("Другое", "Другое"),
    ]
    type_of_employment_list = [
        ("Только в будние дни", "Только в будние дни"),
        ("Только в выходные дни", "Только в выходные дни"),
        ("Любые дни", "Любые дни"),
    ]

    title = models.CharField(verbose_name="Название вакансии", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="specialist_user", null=True)
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    experience = models.CharField(verbose_name="Опыт работы", choices=experience_list, max_length=50)
    type_of_employment = models.CharField(verbose_name="Тип занятости", choices=type_of_employment_list, max_length=50)
    special_conditions = models.CharField(verbose_name="Готов работать с", choices=special_conditions_list, max_length=50)

    def __str__(self):
        return self.title