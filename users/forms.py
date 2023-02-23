from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *






class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'auth_form_input', 'placeholder': 'Адрес электронной почты'}))
    username= forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'auth_form_input', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'auth_form_input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'auth_form_input', 'placeholder': 'Повторите пароль'}))
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2' ]


class ProfileRegisterForm(forms.ModelForm):

    name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'auth_form_input auth_form__user', 'placeholder': 'Имя'}), required=False)
    surname = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'auth_form_input auth_form__user', 'placeholder': 'Фамилия'}), required=False)
    age = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'auth_form_input auth_form__user', 'placeholder': 'Возраст'}), required=False)
    employer = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'auth_form_input auth_form__employer', 'placeholder': 'Название орагнизации'}), error_messages = {'unique':"Выбранное название организации уже используется, выберите другое название"}, required=False, empty_value=None)
    account_type = forms.ChoiceField(label='', choices=Profile.account_type_list,initial="Пользователь" ,widget=forms.RadioSelect(attrs={'class': 'auth_form_choise', 'placeholder': 'Тип аккаунта'}))

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'age', 'employer', 'account_type' ]


class UserLoginForm(forms.Form):
    username= forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'auth_form_input', 'placeholder': 'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'auth_form_input', 'placeholder': 'Пароль'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Адрес электронной почты'}))
 
    class Meta:
        model = User
        fields = ['email']
 

class UserProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label='Имя', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=20, label='Фамилия', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Фамилия'}))
    age = forms.IntegerField(label='Возраст', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Возраст'}))
    image = forms.ImageField(label='', widget = forms.FileInput(attrs={'class': 'my_profile_edit_file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'my_profile_edit_textarea', 'placeholder': 'О себе'}), required=False)
    contacts = forms.CharField(label='Контакты',required=False, widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Контакты'}))
    show_email = forms.ChoiceField(label='', choices=Profile.show_list,initial="Отображение почты" ,widget=forms.Select(attrs={'class': 'my_profile_edit_input'}))
    show_contacts = forms.ChoiceField(label='', choices=Profile.show_list,initial="Отображение контактов" ,widget=forms.Select(attrs={'class': 'my_profile_edit_input'}))

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'age', 'image', 'bio', 'contacts', 'show_email', 'show_contacts']


class EmployerProfileUpdateForm(forms.ModelForm):
    
    employer = forms.CharField(max_length=20, label='Имя', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Название орагнизации'}), error_messages = {'unique':"Выбранное название организации уже используется, выберите другое название"})
    image = forms.ImageField(label='', widget = forms.FileInput(attrs={'class': 'my_profile_edit_file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'my_profile_edit_textarea', 'placeholder': 'О себе'}), required=False)
    contacts = forms.CharField(label='Контакты',required=False, widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Контакты'}))
    show_email = forms.ChoiceField(label='', choices=Profile.show_list,initial="Отображение почты" ,widget=forms.Select(attrs={'class': 'my_profile_edit_input'}))
    show_contacts = forms.ChoiceField(label='', choices=Profile.show_list,initial="Отображение контактов" ,widget=forms.Select(attrs={'class': 'my_profile_edit_input'}))

    class Meta:
        model = Profile
        fields = ['employer', 'image','bio', 'contacts', 'show_email', 'show_contacts']


class ChildrenProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label='Имя', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=20, label='Фамилия', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Фамилия'}))
    age = forms.IntegerField(label='Возраст', widget=forms.TextInput(attrs={'class': 'my_profile_edit_input', 'placeholder': 'Возраст'}))
    image = forms.ImageField(label='', widget = forms.FileInput(attrs={'class': 'my_profile_edit_file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'my_profile_edit_textarea', 'placeholder': 'О себе'}))

    class Meta:
        model = Profile
        fields = ['image','bio']


class PortfolioEditForm(forms.ModelForm):

    title = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Укажите желаемую должность'}))
    about = forms.CharField(label='О себе', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Укажите кратко о себе'}))
    work_experience = forms.CharField(label='Опыт работы', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Расскажите о вашем опыте работы'}))
    education = forms.CharField(label='Образование', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Укажите ваше образование', 'rows':'5'}))
    languages = forms.CharField(label='Языки', widget=forms.Textarea(attrs={'class': 'service_add_input', 'placeholder': 'Укажите языки которыми вы владеете, а так же их уровнь', 'rows':'5'}))
    link = forms.URLField(label='Ссылка на портфолио', widget=forms.TextInput(attrs={'class': 'service_add_input', 'placeholder': 'Вставьте ссылку на ваше портфолио/сайт/облачное хранилище'}), required=False)

    type_of_employment = forms.ChoiceField(choices=User_portfolio.type_of_employment_list, label='Тип занятости', widget=forms.Select(attrs={'class': 'service_add_input'}))
    schedule = forms.ChoiceField(choices=User_portfolio.schedule_list, label='График работы', widget=forms.Select(attrs={'class': 'service_add_input'}))
    special_conditions = forms.ChoiceField(choices=User_portfolio.special_conditions_list, label='Особые условия', widget=forms.Select(attrs={'class': 'service_add_input'}))

    class Meta:
        model = User_portfolio
        fields = ['title', 'about', 'work_experience', 'education', 'languages', 'link', 'type_of_employment', 'schedule', 'special_conditions']
