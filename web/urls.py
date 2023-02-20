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
	path('specialist', views.specialist__page, name='specialist'),
	path('specialist/add', views.specialist_add__page, name='specialist_add'),
	path('specialist/edit/<int:id>', views.specialist_edit__page, name='specialist_edit'),
	path('specialist/delete/<int:id>', views.specialist_delete__page, name='specialist_delete'),
	path('volunteer', views.volunteer__page, name='volunteer'),
	path('volunteer/add', views.volunteer_add__page, name='volunteer_add'),
	path('volunteer/edit/<int:id>', views.volunteer_edit__page, name='volunteer_edit'),
	path('volunteer/delete/<int:id>', views.volunteer_delete__page, name='volunteer_delete'),
	path('needhelp', views.needhelp__page, name='needhelp'),
	path('needhelp/add', views.needhelp_add__page, name='needhelp_add'),
	path('needhelp/edit/<int:id>', views.needhelp_edit__page, name='needhelp_edit'),
	path('needhelp/delete/<int:id>', views.needhelp_delete__page, name='needhelp_delete'),
	path('section', views.section__page, name='section'),
	path('section/add', views.section_add__page, name='section_add'),
	path('section/edit/<int:id>', views.section_edit__page, name='section_edit'),
	path('section/delete/<int:id>', views.section_delete__page, name='section_delete'),
	path('event', views.event__page, name='event'),
	path('event/add', views.event_add__page, name='event_add'),
	path('event/edit/<int:id>', views.event_edit__page, name='event_edit'),
	path('event/delete/<int:id>', views.event_delete__page, name='event_delete'),
	path('favorite', views.favorite__page, name='favorite'),
	path('response', views.response__page, name='response'),
	path('news', views.news__page, name='news'),
	path('news/<int:id>', views.news_about__page, name='news_about'),
	path('info', views.info__page, name='info'),
	path('search', views.search__page, name='search')
	]