"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from trpgassistant import views

urlpatterns = [
    path('', views.title_action, name='title'),
    path('login', views.login_action, name='login'),
    path('register', views.register_action, name='register'),
    path('frontpage', views.front_action, name='frontpage'),
    path('create_character', views.create_character_action, name='create_character'),
    path('view_character/<int:id>', views.view_character_action, name='view_character'),
    path('list_characters', views.list_characters_action, name='list_characters'),
    path('join_game', views.join_game_action, name='join_game'),
    path('add_character', views.add_character_action, name='add_character'),
    path('remove_character', views.remove_character_action, name='remove_character'),
    path('get_all_characters', views.get_all_characters_action, name='get_all_characters'),
    path('add_comment', views.add_comment, name='add_comment')
]
