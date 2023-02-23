from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from web.views import *
from web.models import *
from .models import *
from .forms import *

def user_register(request):
    if request.user.is_authenticated == True:
        return redirect('profile')
        data ={}
    else:
        if request.method == 'POST':
            u_form = UserRegisterForm(request.POST)
            p_form = ProfileRegisterForm(request.POST)

            if u_form.is_valid() and p_form.is_valid():

                #Создание user и profile
                user = u_form.save()
                profile = p_form.save(commit=False)
                profile.user = user
                profile.save()
                
                #Удаление ненужных значений из регистрации
                if profile.account_type == "Пользователь":
                    Profile.objects.filter(user=profile.user).update(employer=None)
                elif profile.account_type == "Детский":
                    Profile.objects.filter(user=profile.user).update(name=None, surname=None, age=None, employer=None)
                elif profile.account_type == "Работодатель":
                    Profile.objects.filter(user=profile.user).update(name=None, surname=None, age=None)

                #username = u_form.cleaned_data.get('username')
                #messages.success(request, f'Создан аккаунт {username}!')
                return redirect('login')
            else:
                print("Error")
        else:
            u_form = UserRegisterForm()
            p_form = ProfileRegisterForm()
        data = {
            'u_form': u_form,
            'p_form': p_form,
        }
    return render(request, 'users/register.html', data)


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('profile')
        data ={}
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        print("Авторизация успешна")
                        return redirect('profile')
                    else:
                        print("Не активен")
                        return HttpResponse('Disabled account')     
                else:
                    print("Неправильно")
                    return HttpResponse('Invalid login')
        else:
            form = UserLoginForm()

        data = {
            'form': form
        }
    return render(request, 'users/login.html', data)


@login_required
def profile(request):
    if request.user.profile.account_type == "Работодатель":
        job = Job.objects.filter(employer__employer=request.user.profile.employer)
        data={
            "Jobs": job
        }
    elif request.user.profile.account_type == "Пользователь":
        portfolio   = User_portfolio.objects.filter(user=request.user)
        specialist = Specialist.objects.filter(user=request.user)
        volunteer = Volunteer.objects.filter(user=request.user)
        needhelp = Needhelp.objects.filter(user=request.user)
        section = Section.objects.filter(user=request.user)
        event = Event.objects.filter(user=request.user)
        data={
            'portfolio'   : portfolio,  
            'specialists': specialist,
            'volunteers': volunteer,
            'needhelps': needhelp,
            'sections': section,
            'events': event
        }
    elif request.user.profile.account_type == "Детский":
        data = {

        }
    else:
        return redirect('home')
    return render(request, 'users/profile.html', data)


def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if request.user.profile.account_type == "Пользователь":
            p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        elif request.user.profile.account_type == "Детский":
            p_form = ChildrenProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        elif request.user.profile.account_type == "Работодатель":
            p_form = EmployerProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        else:
            return redirect('profile')

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')
        else:
            print(u_form.errors, p_form.errors)

    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.profile.account_type == "Пользователь":
            p_form = UserProfileUpdateForm(instance=request.user.profile)
        elif request.user.profile.account_type == "Детский":
            p_form = ChildrenProfileUpdateForm(instance=request.user.profile)
        elif request.user.profile.account_type == "Работодатель":
            p_form = EmployerProfileUpdateForm(instance=request.user.profile)
        else:
            return redirect('profile')

    data = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_edit.html', data)


@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)

    if user.profile.account_type == "Работодатель":

        job_response = []

        #ID работ, на которые откликнулся юзер
        if request.user.is_authenticated == True:
            job_response_queryset = Job_response.objects.filter(user=request.user)
            for el in job_response_queryset:
                job_response.append(el.job.id)

        job = Job.objects.filter(employer__employer=user.profile.employer).order_by('-id')

        data = {
            'Jobs':job,
            'user_profile': user,
            'Job_response': job_response
        }
    elif user.profile.account_type == "Пользователь":

        favorite = []
        if request.user.is_authenticated == True:
            favorite_specialist = user_favorite_list(request.user, "Специалисты")
            favorite_volunteer = user_favorite_list(request.user, "Волонтерство")
            favorite_needhelp = user_favorite_list(request.user, "Нуждаются в помощи")
            favorite_section = user_favorite_list(request.user, "Секции")
            favorite_event = user_favorite_list(request.user, "Мероприятия")


        if request.method == "POST" and request.user.is_authenticated == True:
            if request.POST['service_id'] and request.POST['service_name']:
                change_favorite(
                    request.user,
                    request.POST['service_name'],
                    request.POST['service_id']
                    )
                return redirect(f'/user/{user.username}')

        specialist = Specialist.objects.filter(user=user)
        volunteer = Volunteer.objects.filter(user=user)
        needhelp = Needhelp.objects.filter(user=user)
        section = Section.objects.filter(user=user)
        event = Event.objects.filter(user=user)
        data = {
            'user_profile': user,
            'favorite_specialist': favorite_specialist,
            'favorite_volunteer': favorite_volunteer,
            'favorite_needhelp': favorite_needhelp,
            'favorite_section': favorite_section,
            'favorite_event': favorite_event,
            'specialists': specialist,
            'volunteers': volunteer,
            'needhelps': needhelp,
            'sections': section,
            'events': event
        }
    return render(request, 'users/user.html', data)