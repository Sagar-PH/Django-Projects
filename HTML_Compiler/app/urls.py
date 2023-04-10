"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('base/', views.base, name='base'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('logout/', views.log_out, name='logout'),
    path('cardform/', views.cardform, name='cardform'),
    path('frontend_detail/<int:frontend_id>/', views.frontend_detail, name='frontend_detail'),
    path('frontend_display/<int:frontend_id>/', views.frontend_display, name='frontend_display'),
    path('password_change/',
     auth_views.PasswordChangeView.as_view(template_name="accounts1/password_change.html"),
      name="password_change"),

    path('password_change/done/',
     auth_views.PasswordChangeDoneView.as_view(template_name="accounts1/password_change_done.html"),
      name="password_change_done"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts1/password_reset.html"),
      name="reset_password"),

    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name="accounts1/password_reset_sent.html"),
     name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts1/password_reset_form.html"),
      name="password_reset_confirm"),

    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name="accounts1/password_reset_done.html"),
     name="password_reset_complete"),

    path('<int:pk>/delete', UserDelete.as_view(template_name="accounts1/delete_account.html"), name='delete_account'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
