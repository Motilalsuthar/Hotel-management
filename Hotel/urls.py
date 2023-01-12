"""Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hotelapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view),
    path('add/', add_view),
    path('display/', display_view),
    path('room/', room_view),
    path('roomdisplay/', rdisplay_view),
    path('user_update/', upuser_views),
    path('update/<int:u>', updateuser_view),
    path('room_update/', uproom_views),
    path('roomupdate/<int:u>', updateroom_view),
    path('user_delete/', deluser_views),
    path('delete/', deleteuser_view),
    path('warn/<int:j>', warning),
    path('delroom/', delroom_views),
    path('warn1/<int:d>', warning1),
]
