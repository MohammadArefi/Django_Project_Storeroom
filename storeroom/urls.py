"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from storeroom.views import *

app_name = 'storeroom'

urlpatterns = [
    path('', index, name='index'),  # render
    path('input', input_record, name='input'),    # render
    path('register', register, name='register'),
    path('search', search_record, name='search'),     # render
    path('search_status', search_status, name='search_status'),
    path('update_status', update_status, name='update_status'),
    path('update', update_record, name='update'),     # render
    path('report', report, name='report'),    # render
    path('reporting', reporting, name='reporting'),
    path('login/', Login, name='Login'),
    path('login_user/', loginuser, name='login_user'),
    path('logout/', logoutuser, name='logout'),
]
