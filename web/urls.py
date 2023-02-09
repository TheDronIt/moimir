from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	path('', views.index__page, name='home'),
	path('job', views.job__page, name='job'),
	path('job/response', views.job_response, name='job_response'),
	path('job/show-response/<int:id>', views.job_show_response__page, name='job_show_response'),
	path('job/add', views.job_add__page, name='job_response'),
	path('job/edit/<int:id>', views.job_edit__page, name='job_edit'),
	path('job/delete/<int:id>', views.job_delete__page, name='job_delete'),
	path('search', views.search__page, name='search')
	]