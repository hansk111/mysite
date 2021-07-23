"""config URL Configuration

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
from board import views


app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    
    path('golfrule', views.golfrule, name='golfrule'),
    path('screengolf', views.screengolf, name='screengolf'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('vote/post/<int:post_id>/', views.vote_post, name='vote_post'),
    path('vote/comment/<int:comment_id>/', views.vote_comment, name='vote_comment'),
    path('category/<int:category_id>', views.board_category, name='board_category'),
   
]
