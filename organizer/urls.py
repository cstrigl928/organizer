"""organizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from tasks import views as task_view
from journal import views as journal_views
from enviroment import views as enviroment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',enviroment_views.home),
    path('about/',enviroment_views.about),
    path('join/', enviroment_views.join),
    path('login/', enviroment_views.user_login),
    path('logout/', enviroment_views.user_logout),
    path('journal/', journal_views.journal),
 	path('journal/add/', journal_views.add),
    path('journal/edit/<int:id>/', journal_views.edit),
]
