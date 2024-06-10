"""
URL configuration for django_jobs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users import views

urlpatterns = [
    path('register_applicant/', views.register_applicant, name= 'register'),
    path('register_recruiter/', views.register_recruiter, name= 'register_recruiter'),
    path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('', views.proxy, name= 'proxy'),
    path('applicant_dashboard', views.applicant_dashboard, name= 'applicant_dashboard'),
    path('recruiter_dashboard', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('admin/', admin.site.urls),
]
