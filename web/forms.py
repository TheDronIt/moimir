from django import forms
from .models import *

class JobFilterForm(forms.ModelForm):

    type_of_employment = forms.ChoiceField(label='Тип занятости', choices=Job.type_of_employment_list ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    schedule = forms.ChoiceField(label='График работы', choices=Job.schedule_list ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    experience = forms.ChoiceField(label='Опыт работы', choices=Job.experience_list ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    special_conditions = forms.ChoiceField(label='Особые условия', choices=Job.special_conditions_list ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))

    class Meta:
        model = Job
        fields = ['type_of_employment', 'schedule', 'experience', 'special_conditions' ]



class JobAddForm(forms.ModelForm):

    title = forms.CharField(label='Название вакансии', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название вакансии'}))
    min_salary = forms.IntegerField(label='ЗП от', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'ЗП от'}))
    max_salary = forms.IntegerField(label='ЗП до', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'ЗП до'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Описание'}))
    
    type_of_employment = forms.ChoiceField(choices=Job.type_of_employment_list, label='Тип занятости', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Тип занятости'}))
    schedule = forms.ChoiceField(choices=Job.schedule_list, label='График работы', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'График работы'}))
    experience = forms.ChoiceField(choices=Job.experience_list, label='Опыт работы', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Опыт работы'}))
    special_conditions = forms.ChoiceField(choices=Job.special_conditions_list, label='Особые условия', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Особые условия'}))

    class Meta:
        model = Job
        fields = ['title', 'min_salary', 'max_salary', 'description', 'type_of_employment', 'schedule', 'experience', 'special_conditions']




class SpecialistFilterForm(forms.ModelForm):

    experience = forms.ChoiceField(label='Опыт работы', choices=Specialist.experience_list ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    type_of_employment = forms.ChoiceField(label='Тип занятости', choices=Specialist.type_of_employment_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    special_conditions = forms.ChoiceField(label='Готов работать с', choices=Specialist.special_conditions_list ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))

    class Meta:
        model = Specialist
        fields = ['experience', 'type_of_employment', 'special_conditions']


class SpecialistEditForm(forms.ModelForm):

    title = forms.CharField(label='Название услуги специалиста', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название услуги специалиста'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Описание'}))
    
    experience = forms.ChoiceField(choices=Specialist.experience_list, label='Опыт работы', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Опыт работы'}))
    type_of_employment = forms.ChoiceField(choices=Specialist.type_of_employment_list, label='Тип занятости', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Тип занятости'}))
    special_conditions = forms.ChoiceField(choices=Specialist.special_conditions_list, label='Готов работать с', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Особые условия'}))

    class Meta:
        model = Specialist
        fields = ['title', 'description', 'type_of_employment', 'special_conditions', 'experience']



class VolunteerFilterForm(forms.ModelForm):

    type_of_employment = forms.ChoiceField(label='Тип занятости', choices=Volunteer.type_of_employment_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    work_with = forms.ChoiceField(label='Готов помочь', choices=Volunteer.work_with_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))

    class Meta:
        model = Volunteer
        fields = ['type_of_employment', 'work_with']


class VolunteerEditForm(forms.ModelForm):

    title = forms.CharField(label='Название услуги волонтера', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название услуги волонтера'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Описание'}))
    
    type_of_employment = forms.ChoiceField(choices=Volunteer.type_of_employment_list, label='Тип занятости', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Тип занятости'}))
    work_with = forms.ChoiceField(choices=Volunteer.work_with_list, label='Готов помочь', widget=forms.Select(attrs={'class': 'service_add_input', 'placeholder': 'Особые условия'}))

    class Meta:
        model = Volunteer
        fields = ['title', 'description', 'type_of_employment', 'work_with']



class NeedhelpFilterForm(forms.ModelForm):

    support_type = forms.ChoiceField(label='Способ помочь', choices=Needhelp.support_type_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))

    class Meta:
        model = Needhelp
        fields = ['support_type']


class NeedhelpEditForm(forms.ModelForm):

    title = forms.CharField(label='Название заголовка', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название заголовка'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Описание'}))
    
    support_type = forms.ChoiceField(choices=Needhelp.support_type_list, label='Способ помочь', widget=forms.Select(attrs={'class': 'service_add_input'}))

    class Meta:
        model = Needhelp
        fields = ['title', 'description', 'support_type']



class SectionFilterForm(forms.ModelForm):

    event_theme = forms.ChoiceField(label='Тема', choices=Section.event_theme_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))
    age_limit = forms.ChoiceField(label='Возрастное ограничение', choices=Section.age_limit_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))

    class Meta:
        model = Section
        fields = ['event_theme', 'age_limit']


class SectionEditForm(forms.ModelForm):

    title = forms.CharField(label='Название секции', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название секции'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Описание'}))
    
    event_theme = forms.ChoiceField(choices=Section.event_theme_list, label='Тема секции', widget=forms.Select(attrs={'class': 'service_add_input'}))
    age_limit = forms.ChoiceField(choices=Section.age_limit_list, label='Возрастное ограничение', widget=forms.Select(attrs={'class': 'service_add_input'}))

    class Meta:
        model = Section
        fields = ['title', 'description', 'event_theme', 'age_limit']



class EventFilterForm(forms.ModelForm):

    event_theme = forms.ChoiceField(label='Тема', choices=Event.event_theme_list, widget=forms.CheckboxSelectMultiple(attrs={'class': 'services_filter_el'}))

    class Meta:
        model = Event
        fields = ['event_theme']


class EventEditForm(forms.ModelForm):

    title = forms.CharField(label='Название мероприятия', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название мероприятия'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Описание'}))
    
    event_location = forms.CharField(label='Адрес мероприятия', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Адрес мероприятия'}))
    event_date = forms.DateField(label='Дата мероприятия', widget=forms.DateInput(attrs={'class': 'service_add_input', 'type': 'date', }))
    event_time = forms.TimeField(label='Дата мероприятия', widget=forms.TimeInput(attrs={'class': 'service_add_input', 'type': 'time' }))

    event_theme = forms.ChoiceField(choices=Event.event_theme_list, label='Тема мероприятия', widget=forms.Select(attrs={'class': 'service_add_input'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'event_location', 'event_date', 'event_time', 'event_theme']