from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name='login'),
    path('profile/<str:pk>/',views.userProfile, name='userProfile'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('',views.Home, name='home'),
    path('room/<str:pk>/',views.room, name='Room'),
    path('createroom/',views.createRoom, name='createRoom'),
    path('updateroom/<str:pk>',views.updateRoom, name='updateRoom'),
    path('deleteroom/<str:pk>',views.deleteRoom, name='deleteRoom'),
    path('deleteMessage/<str:pk>',views.deleteMessage, name='delete-message'),
    path('updateUser/',views.updateUser, name='updateUser'),
    path('topics/',views.topicsPage, name='topics'),
    path('activityPage/',views.activityPage, name='activityPage'),
]
