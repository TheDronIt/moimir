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

    title = models.CharField(verbose_name="Название вакансии", max_length=100)
    employer = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Аккаунт организации")
    min_salary = models.IntegerField(verbose_name="ЗП от")
    max_salary = models.IntegerField(verbose_name="ЗП до")
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)
    description = models.TextField(verbose_name="Описание", max_length=1000)

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
        ("Нуждаются в помощи", "Нуждаются в помощи"),
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

    title = models.CharField(verbose_name="Название услуги", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="specialist_user", null=True)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    experience = models.CharField(verbose_name="Опыт работы", choices=experience_list, max_length=50)
    type_of_employment = models.CharField(verbose_name="Тип занятости", choices=type_of_employment_list, max_length=50)
    special_conditions = models.CharField(verbose_name="Готов работать с", choices=special_conditions_list, max_length=50)

    def __str__(self):
        return self.title



class Volunteer(models.Model):
    class Meta:
        verbose_name = 'Волонтеры'
        verbose_name_plural = 'Волонтеры'

    type_of_employment_list = [
        ("Только в будние дни", "Только в будние дни"),
        ("Только в выходные дни", "Только в выходные дни"),
        ("Любые дни", "Любые дни"),
    ]
    work_with_list = [
        ("Ребенку", "Ребенку"),
        ("Взрослому", "Взрослому"),
        ("Пожилому", "Пожилому"),
        ("Всем", "Всем")    
    ]

    title = models.CharField(verbose_name="Название услуги волонтера", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="volunteer_user", null=True)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    type_of_employment = models.CharField(verbose_name="Тип занятости", choices=type_of_employment_list, max_length=50)
    work_with = models.CharField(verbose_name="Готов помочь", choices=work_with_list, max_length=50)

    def __str__(self):
        return self.title



class Needhelp(models.Model):
    class Meta:
        verbose_name = 'Нуждаются в помощи'
        verbose_name_plural = 'Нуждаются в помощи'

    support_type_list = [
        ("Финансы", "Финансы"),
        ("Услуга", "Услуга"),
        ("Прочее", "Прочее")
    ]

    title = models.CharField(verbose_name="Название услуги волонтера", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="needhelp_user", null=True)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    support_type = models.CharField(verbose_name="Способ помочь", choices=support_type_list, max_length=50)

    def __str__(self):
        return self.title



class Section(models.Model):
    class Meta:
        verbose_name = 'Секции'
        verbose_name_plural = 'Секции'

    event_theme_list = [
        ("Спорт", "Спорт"),
        ("Волонтерство", "Волонтерство"),
        ("Игры", "Игры"),
        ("Театральное искусство", "Театральное искусство"),
        ("Образование", "Образование"),
        ("Творчество", "Творчество"),
        ("Другое", "Другое")
    ]
    age_limit_list = [
        ("Для детей", "Для детей"),
        ("Для взрослых", "Для взрослых"),
        ("Без ограничений", "Без ограничений")
    ]

    title = models.CharField(verbose_name="Название секции", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="sections_user", null=True)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    event_theme = models.CharField(verbose_name="Тема секции", choices=event_theme_list, max_length=50)
    age_limit = models.CharField(verbose_name="Возрастное ограничение", choices=age_limit_list, max_length=50)

    def __str__(self):
        return self.title


class Event(models.Model):
    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'

    display_status_list = [
        ("Отображать", "Отображать"),
        ("Скрывать", "Скрывать")
    ]

    event_theme_list = [
        ("Спорт", "Спорт"),
        ("Цирк", "Цирк"),
        ("Городские события", "Городские события"),
        ("Игры и квесты", "Игры и квесты"),
        ("Театры", "Театры"),
        ("Концерты", "Концерты"),
        ("Музеи и галереи", "Музеи и галереи"),
        ("Экскурсии ", "Экскурсии "),
        ("Обучение ", "Обучение "),
        ("Творчество", "Творчество")
    ]

    title = models.CharField(verbose_name="Название мероприятия", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="event_user", null=True)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    event_location = models.CharField(verbose_name="Адрес мероприятия", max_length=50)
    event_date = models.DateField(verbose_name='Дата мероприятия')
    event_time = models.TimeField(verbose_name='Время мероприятия')

    event_theme = models.CharField(verbose_name="Тема мероприятия", choices=event_theme_list, max_length=50)

    display_status = models.CharField(verbose_name="Статус отображения", choices=display_status_list, default="Скрывать" ,max_length=50)

    def __str__(self):
        return self.title


class InfoCategory(models.Model):
    class Meta:
        verbose_name = 'Категории полезной информации'
        verbose_name_plural = 'Категории полезной информации'

    name = models.CharField(verbose_name="Название", max_length=50)

    def __str__(self):
        return str(self.name)


class InfoFile(models.Model):
    class Meta:
        verbose_name = 'Полезная информация'
        verbose_name_plural = 'Полезная информация'

    visibility_list = [
        ("Отображать", "Отображать"),
        ("Не отображать", "Не отображать")
    ]

    name = models.CharField(verbose_name="Название", max_length=50)
    category = models.ForeignKey(InfoCategory, on_delete=models.SET_NULL, null=True, blank=True,related_name='infocategory_category', verbose_name="Категория")
    file = models.FileField(upload_to='info/file/',null=True, verbose_name="Фаил")
    visibility = models.CharField(max_length=50, choices=visibility_list, default="Отображать", verbose_name="Отображение")

    def __str__(self):
        return str(self.name)



class News(models.Model):
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    title = models.CharField(verbose_name="Заголовок", max_length=50)
    image = models.ImageField(verbose_name="Изображение", upload_to='news/')
    date = models.DateField(verbose_name='Дата', default=datetime.now, blank=True)

    def __str__(self):
        return str(self.title)