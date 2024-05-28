# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('dashboard',views.userDashboard),
    path('profile',views.profile),
    path('edit',views.edit),
    path('status',views.leaveStatus),
    path('apply-leave',views.applyLeave),
    # admin
    path('admin-dashboard',views.adminDashboard),
    path('users',views.usersList),
    path('leaves',views.leaves),
    path('attendance',views.attendance)
]
