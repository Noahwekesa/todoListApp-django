"""
URL configuration for todo project.

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
from django.urls import path
from tasks import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="home"),
    path('submit_todo/', views.submit_todo, name='submit-todo'),
    path('complete_todo/<int:pk>/', views.complete_todo, name='complete-todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
]
