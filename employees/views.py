from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee
from .forms import EmployeeForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")



# Logout

def user_logout(request):

    logout(request)

    return redirect('login')



# Dashboard

@login_required
def dashboard(request):

    total_employees = Employee.objects.count()

    return render(
        request,
        'dashboard.html',
        {
            'total_employees': total_employees
        }
    )


# Add Employee

@login_required
def add_employee(request):

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            form.save()

            return redirect('employee_list')


    else:

        form = EmployeeForm()



    return render(
        request,
        'employees/add_employee.html',
        {
            'form': form
        }
    )



# Employee List

@login_required
def employee_list(request):

    employees = Employee.objects.all()


    return render(
        request,
        'employees/employee_list.html',
        {
            'employees': employees
        }
    )



# Employee Detail

@login_required
def employee_detail(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )


    return render(
        request,
        'employees/employee_detail.html',
        {
            'employee': employee
        }
    )



# Edit Employee

@login_required
def edit_employee(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )


    form = EmployeeForm(
        request.POST or None,
        request.FILES or None,
        instance=employee
    )


    if form.is_valid():

        form.save()

        return redirect('employee_list')



    return render(
        request,
        'employees/edit_employee.html',
        {
            'form': form
        }
    )



# Delete Employee

@login_required
def delete_employee(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )


    employee.delete()


    return redirect('employee_list')


