from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def index__page(request):
    data = {
        
    }
    return render(request, 'web/page/index.html', data)


def job__page(request):

    filter_form = JobFilterForm()
    job_response = []

    #ID работ, на которые откликнулся юзер
    if request.user.is_authenticated == True:
        job_response_queryset = Job_response.objects.filter(user=request.user)
        for el in job_response_queryset:
            job_response.append(el.job.id)
    
    #Фильтрация по значеням из GET (фильтрация через форму)
    if request.method == 'GET' and len(request.GET) > 0:
        query_dict = dict(request.GET)
        query_dict.pop("csrfmiddlewaretoken")
        
        query_dict = {f'{name}__in': query_dict[name]  for name in query_dict if query_dict[name]}

        job = Job.objects.filter(**query_dict).order_by('-id')
    else:
        job = Job.objects.all().order_by('-id')


    data = {
        'filter_form': filter_form,
        'Jobs': job,
        'Job_response': job_response
    }
    return render(request, 'web/page/job.html', data)


@login_required
def job_add__page(request):
    if request.user.profile.account_type == "Работодатель":
        if request.method == 'POST':
            form = JobAddForm(request.POST)

            if form.is_valid():
                updated_form = form.save(commit=False)
                updated_form.employer = Profile.objects.get(id=request.user.profile.id)
                updated_form.save()
                return redirect('job')
        else:
            form = JobAddForm()
        
        data = {
                'form': form
            }
        return render(request, 'web/page/service_edit.html', data)
    else:
        return redirect('job')
        


@login_required
def job_response(request):
    
    #Получаем данные для сохранения по данным POST
    if request.method == "POST":

        response_type = request.POST['response_type']
        #Отклик
        if response_type == "save":
            try:
                job_id = int(request.POST['job_id'])
                job = Job.objects.get(pk=job_id)
                user = User.objects.get(username=request.user.username)
            except:
                return redirect('home')

            #Проверяем на отстутствие записи с такими же данными
            job_response_is_created = Job_response.objects.filter(user=user, job=job)
            if len(job_response_is_created) == 0:
                Job_response(user=user, job=job).save()
        #Отмена отклика
        elif response_type == "cancel":
            try:
                job_id = int(request.POST['job_id'])
                job = Job.objects.get(pk=job_id)
                user = User.objects.get(username=request.user.username)
            except:
                return redirect('home')

            #Проверяем на отстутствие записи с такими же данными
            job_response_is_created = Job_response.objects.filter(user=user, job=job)
            if len(job_response_is_created) >= 1:
                Job_response.objects.get(user =user, job=job).delete()
        
    return redirect('job')



@login_required
def job_edit__page(request, id):
    if request.user.profile.account_type == "Работодатель":
        
        job = Job.objects.get(id=id)
        
        #Проверка на владение записью
        if job.employer.employer == request.user.profile.employer:

            if request.method == 'POST':
                form = JobAddForm(request.POST, instance=job)
                if form.is_valid():
                    form.save()
                    return redirect('job')
            else:
                form = JobAddForm(instance=job)

            data ={
                'form': form
            }
            return render(request, 'web/page/service_edit.html', data)
    return redirect('job')



@login_required
def job_show_response__page(request, id):
    if request.user.profile.account_type == "Работодатель":
        
        job = Job.objects.get(id=id)
        
        #Проверка на владение записью
        if job.employer.employer == request.user.profile.employer:
            responses = Job_response.objects.filter(job=job)
            data = {
                "job": job,
                "responses":responses
            }
            return render(request, 'web/page/job_show-response.html', data)

    return redirect('job')



@login_required
def job_delete__page(request, id):
    if request.user.profile.account_type == "Работодатель":
        job = Job.objects.get(id=id)
        #Проверка на владение записью
        if job.employer.employer == request.user.profile.employer:

            if request.method == "POST" and request.POST['delete_confirmation']:
                if request.POST['delete_confirmation'] == "delete_accept":
                    job.delete()
            else:
                response_value = Job_response.objects.filter(job=job).count()
                data ={
                    "Job": job,
                    "response_value": response_value,
                }
                return render(request, 'web/page/job_delete.html', data)
    return redirect('job')


def search__page(request):
    job_response = []
    answer = []
    favorite = []
    query = ""
    service_type = None
    if request.GET['service'] and request.GET['q']:
        query = request.GET['q']

        #Поиск запроса по нужной базе
        if request.GET['service'] == "job":
            #ID работ, на которые откликнулся юзер
            if request.user.is_authenticated == True:
                job_response_queryset = Job_response.objects.filter(user=request.user)
                for el in job_response_queryset:
                    job_response.append(el.job.id)
            service_type = "job"
            answer = Job.objects.filter(title__icontains=query).order_by('-id') | Job.objects.filter(description__icontains=query).order_by('-id')
        
        elif request.GET['service'] == "specialist":
            if request.user.is_authenticated == True:
                favorite = user_favorite_list(request.user, "Специалисты")
                if request.method == "POST" and request.user.is_authenticated == True:
                    if request.POST['service_id'] and request.POST['service_name']:
                        change_favorite(
                            request.user,
                            request.POST['service_name'],
                            request.POST['service_id']
                            )
                        return redirect('specialist')
            service_type = "specialist"
            answer = Specialist.objects.filter(title__icontains=query).order_by('-id') | Specialist.objects.filter(description__icontains=query).order_by('-id')

        elif request.GET['service'] == "volunteer":
            if request.user.is_authenticated == True:
                favorite = user_favorite_list(request.user, "Волонтерство")
                if request.method == "POST" and request.user.is_authenticated == True:
                    if request.POST['service_id'] and request.POST['service_name']:
                        change_favorite(
                            request.user,
                            request.POST['service_name'],
                            request.POST['service_id']
                            )
                        return redirect('volunteer')
            service_type = "volunteer"
            answer = Volunteer.objects.filter(title__icontains=query).order_by('-id') | Volunteer.objects.filter(description__icontains=query).order_by('-id')


    data = {
        'query':query,
        'service_type': service_type,
        'answer': answer,
        'Job_response': job_response,
        'favorites': favorite
    }
    return render(request, 'web/page/search.html', data)



def specialist__page(request): 
    favorite = []
    if request.user.is_authenticated == True:
        favorite = user_favorite_list(request.user, "Специалисты")

    if request.method == "POST" and request.user.is_authenticated == True:
        if request.POST['service_id'] and request.POST['service_name']:
            change_favorite(
                request.user,
                request.POST['service_name'],
                request.POST['service_id']
                )
            return redirect('specialist')

    filter_form = SpecialistFilterForm()
    #Фильтрация по значеням из GET (фильтрация через форму)
    if request.method == 'GET' and len(request.GET) > 0:
        query_dict = dict(request.GET)
        query_dict.pop("csrfmiddlewaretoken")
        
        query_dict = {f'{name}__in': query_dict[name]  for name in query_dict if query_dict[name]}

        specialist = Specialist.objects.filter(**query_dict).order_by('-id')
    else:
        specialist = Specialist.objects.all().order_by('-id')

        
    data = {
        'filter_form': filter_form,
        'specialists': specialist,
        'favorites': favorite
    }
    return render(request, 'web/page/specialist.html', data)


def specialist_add__page(request):
    if request.user.profile.account_type == "Пользователь":
        if request.method == 'POST':
            form = SpecialistEditForm(request.POST)

            if form.is_valid():
                updated_form = form.save(commit=False)
                updated_form.user = request.user #User.objects.get(user=request.user.profile.id)
                updated_form.save()
                
                return redirect('specialist')
        else:
            form = SpecialistEditForm()
        
        data = {
                'form': form
            }
        return render(request, 'web/page/service_edit.html', data)
    else:
        return redirect('specialist')



@login_required
def specialist_edit__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        
        specialist = Specialist.objects.get(id=id)
        
        #Проверка на владение записью
        if specialist.user.username == request.user.username:

            if request.method == 'POST':
                form = SpecialistEditForm(request.POST, instance=specialist)
                if form.is_valid():
                    form.save()
                    return redirect('specialist')
            else:
                form = SpecialistEditForm(instance=specialist)

            data ={
                'form': form
            }
            return render(request, 'web/page/service_edit.html', data)
    return redirect('specialist')



@login_required
def specialist_delete__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        specialist = Specialist.objects.get(id=id)
        #Проверка на владение записью
        if specialist.user == request.user:
            if request.method == "POST" and request.POST['delete_confirmation']:
                if request.POST['delete_confirmation'] == "delete_accept":
                    specialist.delete()
            else:
                data ={
                    "specialist": specialist,
                }
                return render(request, 'web/page/specialist_delete.html', data)
    return redirect('specialist')





def volunteer__page(request):
    favorite = []
    if request.user.is_authenticated == True:
        favorite = user_favorite_list(request.user, "Волонтерство")
    if request.method == "POST" and request.user.is_authenticated == True:
        if request.POST['service_id'] and request.POST['service_name']:
            change_favorite(
                request.user,
                request.POST['service_name'],
                request.POST['service_id']
                )
            return redirect('volunteer')
    filter_form = VolunteerFilterForm()
    #Фильтрация по значеням из GET (фильтрация через форму)
    if request.method == 'GET' and len(request.GET) > 0:
        query_dict = dict(request.GET)
        query_dict.pop("csrfmiddlewaretoken")
        query_dict = {f'{name}__in': query_dict[name]  for name in query_dict if query_dict[name]}
        volunteer = Volunteer.objects.filter(**query_dict).order_by('-id')
    else:
        volunteer = Volunteer.objects.all().order_by('-id')

    data = {
        'filter_form': filter_form,
        'volunteers': volunteer,
        'favorites': favorite
    }
    return render(request, 'web/page/volunteer.html', data)


def volunteer_add__page(request):
    if request.user.profile.account_type == "Пользователь":
        if request.method == 'POST':
            form = VolunteerEditForm(request.POST)
            if form.is_valid():
                updated_form = form.save(commit=False)
                updated_form.user = request.user #User.objects.get(user=request.user.profile.id)
                updated_form.save()
                return redirect('volunteer')
        else:
            form = VolunteerEditForm()
        
        data = {
                'form': form
            }
        return render(request, 'web/page/service_edit.html', data)
    else:
        return redirect('volunteer')


@login_required
def volunteer_edit__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        volunteer = Volunteer.objects.get(id=id)
        #Проверка на владение записью
        if volunteer.user.username == request.user.username:
            if request.method == 'POST':
                form = VolunteerEditForm(request.POST, instance=volunteer)
                if form.is_valid():
                    form.save()
                    return redirect('volunteer')
            else:
                form = VolunteerEditForm(instance=volunteer)

            data ={
                'form': form
            }
            return render(request, 'web/page/service_edit.html', data)
    return redirect('volunteer')


@login_required
def volunteer_delete__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        volunteer = Volunteer.objects.get(id=id)
        #Проверка на владение записью
        if volunteer.user == request.user:
            if request.method == "POST" and request.POST['delete_confirmation']:
                if request.POST['delete_confirmation'] == "delete_accept":
                    volunteer.delete()
            else:
                data ={
                    "volunteer": volunteer,
                }
                return render(request, 'web/page/volunteer_delete.html', data)
    return redirect('volunteer')




def needhelp__page(request):
    favorite = []
    if request.user.is_authenticated == True:
        favorite = user_favorite_list(request.user, "Нуждаются в помощи")
    if request.method == "POST" and request.user.is_authenticated == True:
        if request.POST['service_id'] and request.POST['service_name']:
            change_favorite(
                request.user,
                request.POST['service_name'],
                request.POST['service_id']
                )
            return redirect('needhelp')
    filter_form = NeedhelpFilterForm()
    #Фильтрация по значеням из GET (фильтрация через форму)
    if request.method == 'GET' and len(request.GET) > 0:
        query_dict = dict(request.GET)
        query_dict.pop("csrfmiddlewaretoken")
        query_dict = {f'{name}__in': query_dict[name]  for name in query_dict if query_dict[name]}
        needhelp = Needhelp.objects.filter(**query_dict).order_by('-id')
    else:
        needhelp = Needhelp.objects.all().order_by('-id')
    data = {
        'filter_form': filter_form,
        'needhelps': needhelp,
        'favorites': favorite
    }
    return render(request, 'web/page/needhelp.html', data)


def needhelp_add__page(request):
    if request.user.profile.account_type == "Пользователь":
        if request.method == 'POST':
            form = NeedhelpEditForm(request.POST)
            if form.is_valid():
                updated_form = form.save(commit=False)
                updated_form.user = request.user #User.objects.get(user=request.user.profile.id)
                updated_form.save()  
                return redirect('needhelp')
        else:
            form = NeedhelpEditForm()
        
        data = {
                'form': form
            }
        return render(request, 'web/page/service_edit.html', data)
    else:
        return redirect('needhelp')


@login_required
def needhelp_edit__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        needhelp = Needhelp.objects.get(id=id)
        #Проверка на владение записью
        if needhelp.user.username == request.user.username:
            if request.method == 'POST':
                form = NeedhelpEditForm(request.POST, instance=needhelp)
                if form.is_valid():
                    form.save()
                    return redirect('needhelp')
            else:
                form = NeedhelpEditForm(instance=needhelp)

            data ={
                'form': form
            }
            return render(request, 'web/page/service_edit.html', data)
    return redirect('needhelp')


@login_required
def needhelp_delete__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        needhelp = Needhelp.objects.get(id=id)
        #Проверка на владение записью
        if needhelp.user == request.user:
            if request.method == "POST" and request.POST['delete_confirmation']:
                if request.POST['delete_confirmation'] == "delete_accept":
                    needhelp.delete()
            else:
                data ={
                    "needhelp": needhelp,
                }
                return render(request, 'web/page/needhelp_delete.html', data)
    return redirect('needhelp')




def section__page(request):
    favorite = []
    if request.user.is_authenticated == True:
        favorite = user_favorite_list(request.user, "Нуждаются в помощи")
    if request.method == "POST" and request.user.is_authenticated == True:
        if request.POST['service_id'] and request.POST['service_name']:
            change_favorite(
                request.user,
                request.POST['service_name'],
                request.POST['service_id']
                )
            return redirect('section')
    filter_form = SectionFilterForm()
    #Фильтрация по значеням из GET (фильтрация через форму)
    if request.method == 'GET' and len(request.GET) > 0:
        query_dict = dict(request.GET)
        query_dict.pop("csrfmiddlewaretoken")
        query_dict = {f'{name}__in': query_dict[name]  for name in query_dict if query_dict[name]}
        section = Section.objects.filter(**query_dict).order_by('-id')
    else:
        section = Section.objects.all().order_by('-id')
    data = {
        'filter_form': filter_form,
        'sections': section,
        'favorites': favorite
    }
    return render(request, 'web/page/section.html', data)


def section_add__page(request):
    if request.user.profile.account_type == "Пользователь":
        if request.method == 'POST':
            form = SectionEditForm(request.POST)
            if form.is_valid():
                updated_form = form.save(commit=False)
                updated_form.user = request.user
                updated_form.save()
                return redirect('section')
        else:
            form = SectionEditForm()
        data = {
                'form': form
            }
        return render(request, 'web/page/service_edit.html', data)
    else:
        return redirect('section')


@login_required
def section_edit__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        section = Section.objects.get(id=id)
        #Проверка на владение записью
        if section.user.username == request.user.username:
            if request.method == 'POST':
                form = SectionEditForm(request.POST, instance=section)
                if form.is_valid():
                    form.save()
                    return redirect('section')
            else:
                form = SectionEditForm(instance=section)

            data ={
                'form': form
            }
            return render(request, 'web/page/service_edit.html', data)
    return redirect('section')


@login_required
def section_delete__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        section = Section.objects.get(id=id)
        #Проверка на владение записью
        if section.user == request.user:
            if request.method == "POST" and request.POST['delete_confirmation']:
                if request.POST['delete_confirmation'] == "delete_accept":
                    section.delete()
            else:
                data ={
                    "section": section,
                }
                return render(request, 'web/page/section_delete.html', data)
    return redirect('section')



def event__page(request):
    favorite = []
    if request.user.is_authenticated == True:
        favorite = user_favorite_list(request.user, "Мероприятия")
    if request.method == "POST" and request.user.is_authenticated == True:
        if request.POST['service_id'] and request.POST['service_name']:
            change_favorite(
                request.user,
                request.POST['service_name'],
                request.POST['service_id']
                )
            return redirect('event')
    filter_form = EventFilterForm()
    #Фильтрация по значеням из GET (фильтрация через форму)
    if request.method == 'GET' and len(request.GET) > 0:
        query_dict = dict(request.GET)
        query_dict.pop("csrfmiddlewaretoken")
        query_dict = {f'{name}__in': query_dict[name]  for name in query_dict if query_dict[name]}
        event = Event.objects.filter(**query_dict).order_by('-id')
    else:
        event = Event.objects.all().order_by('-id')
    data = {
        'filter_form': filter_form,
        'events': event,
        'favorites': favorite
    }
    return render(request, 'web/page/event.html', data)


def event_add__page(request):
    if request.user.profile.account_type == "Пользователь":
        if request.method == 'POST':
            form = EventEditForm(request.POST)
            if form.is_valid():
                updated_form = form.save(commit=False)
                updated_form.user = request.user
                updated_form.save()  
                return redirect('event')
        else:
            form = EventEditForm()
        
        data = {
                'form': form
            }
        return render(request, 'web/page/service_edit.html', data)
    else:
        return redirect('event')


@login_required
def event_edit__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        event = Event.objects.get(id=id)
        #Проверка на владение записью
        if event.user.username == request.user.username:
            if request.method == 'POST':
                form = EventEditForm(request.POST, instance=event)
                if form.is_valid():
                    form.save()
                    return redirect('event')
            else:
                form = EventEditForm(instance=event)

            data ={
                'form': form
            }
            return render(request, 'web/page/service_edit.html', data)
    return redirect('event')


@login_required
def event_delete__page(request, id):
    if request.user.profile.account_type == "Пользователь":
        event = Event.objects.get(id=id)
        #Проверка на владение записью
        if event.user == request.user:
            if request.method == "POST" and request.POST['delete_confirmation']:
                if request.POST['delete_confirmation'] == "delete_accept":
                    event.delete()
            else:
                data ={
                    "event": event,
                }
                return render(request, 'web/page/event_delete.html', data)
    return redirect('event')


def news__page(request):
    data ={
    }
    return render(request, 'web/page/news.html', data)


def info__page(request):
    info_category = InfoCategory.objects.all()
    data ={
        'info_categorys': info_category
    }
    return render(request, 'web/page/info.html', data)


@login_required
def favorite__page(request):

    favorite_value = Favorite.objects.filter(user=request.user).count()

    if favorite_value > 0:
        specialist_favorite_id_list =   Favorite.objects.filter(user=request.user, service_name="Специалисты").values_list('service_id', flat=True)
        specialist_favorite_list =      Specialist.objects.filter(id__in=specialist_favorite_id_list)
        volunteer_favorite_id_list =    Favorite.objects.filter(user=request.user, service_name="Волонтерство").values_list('service_id', flat=True)
        volunteer_favorite_list =       Volunteer.objects.filter(id__in=volunteer_favorite_id_list)
        needhelp_favorite_id_list =     Favorite.objects.filter(user=request.user, service_name="Нуждаются в помощи").values_list('service_id', flat=True)
        needhelp_favorite_list =        Needhelp.objects.filter(id__in=needhelp_favorite_id_list)
        section_favorite_id_list =      Favorite.objects.filter(user=request.user, service_name="Секции").values_list('service_id', flat=True)
        section_favorite_list =         Section.objects.filter(id__in=section_favorite_id_list)
        event_favorite_id_list =        Favorite.objects.filter(user=request.user, service_name="Мероприятия").values_list('service_id', flat=True)
        event_favorite_list =           Event.objects.filter(id__in=event_favorite_id_list)
    
        data = {
            'specialist_favorite_id_list': specialist_favorite_id_list,
            'volunteer_favorite_id_list': volunteer_favorite_id_list,
            'needhelp_favorite_id_list': needhelp_favorite_id_list,
            'section_favorite_id_list': section_favorite_id_list,
            'event_favorite_id_list': event_favorite_id_list,

            'specialist_favorite_list': specialist_favorite_list,
            'volunteer_favorite_list': volunteer_favorite_list,
            'needhelp_favorite_list': needhelp_favorite_list,
            'section_favorite_list': section_favorite_list,
            'event_favorite_list': event_favorite_list,

            'favorite_value': favorite_value
        }
    else:
        data = {
            'favorite_value': favorite_value
        }

    return render(request, 'web/page/favorite.html', data)


def change_favorite(user, service_name, service_id):
    print(user, service_name, service_id)
    service_name_list = ["Специалисты", "Волонтерство", "Нуждаются в помощи", 
                        "Мероприятия", "Секции"]
    try:
        user = User.objects.get(username=user)
        print(user)
        favorite = Favorite.objects.filter(user=user, service_name=service_name, service_id=service_id)
        print(favorite)
        if service_name in service_name_list:
            if len(favorite) == 0:
                Favorite(user=user, service_name=service_name, service_id=int(service_id)).save()
            else:
                favorite.delete()
    except:
        return redirect('error')



def user_favorite_list(user, service_name):
    favorite = []
    favorite_queryset = Favorite.objects.filter(user=user, service_name=service_name)
    for el in favorite_queryset:
        favorite.append(el.service_id)  
    return favorite