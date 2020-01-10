"""django_first_project URL Configuration

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
from django.urls import path,include
from .views import *
from firstapp.views import view_authenticate_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_world_view),
    path('test/',hello_world_from_htmlpage),
    path('form/',form_view),
    path('form/add',form_data),
]

urlpatterns += [
    path('firstapp/',include('firstapp.urls'))
]


urlpatterns += [
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/',view_authenticate_user)

]