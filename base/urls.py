from django.urls import path
from . import views

   #pk means primary key
urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),
    
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('update-user/<str:user>', views.updateUser, name='update-user'),
    path('topics/', views.mobileTopics, name='topics'),
    path('activity/', views.mobileActivity, name='activity'),
    
]