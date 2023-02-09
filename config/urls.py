from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.user_register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('user/<str:username>', user_views.user_profile, name='user'),
    path('profile/edit/', user_views.profile_edit, name='profile_edit'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('web.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
