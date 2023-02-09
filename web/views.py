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
        return render(request, 'web/page/job_add.html', data)
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
                Job_response(user =user, job=job).save()
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
            return render(request, 'web/page/job_add.html', data)
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
    answer = []
    query = ""
    service_type = None
    if request.GET['service'] and request.GET['q']:
        query = request.GET['q']

        #Поиск запроса по нужной базе
        if request.GET['service'] == "job":
            service_type = "job"
            answer = Job.objects.filter(title__icontains=query).order_by('-id') | Job.objects.filter(description__icontains=query).order_by('-id')
    
    data = {
        'query':query,
        'service_type': service_type,
        'answer': answer
    }
    return render(request, 'web/page/search.html', data)


