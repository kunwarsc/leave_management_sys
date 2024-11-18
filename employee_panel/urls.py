# urls.py

from django.urls import path

from . import views
from .views import leave_history, apply_leave, change_password

app_name='employee_panel'

urlpatterns = [
    path('leave_history/', leave_history, name='leave_history'),
    path('apply_leave/', apply_leave, name='apply_leave'),
    path('logout/', views.logout, name='logout'),

    
]
