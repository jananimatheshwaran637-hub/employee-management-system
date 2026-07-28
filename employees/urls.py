from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Home
    path('', lambda request: redirect('login'), name='home'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Employee Management
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:id>/edit/', views.edit_employee, name='edit_employee'),
    path('employees/<int:id>/delete/', views.delete_employee, name='delete_employee'),
]