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

    title = forms.CharField(max_length=20, label='Название вакансии', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Название вакансии'}))
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
