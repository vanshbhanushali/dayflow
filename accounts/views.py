from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from employees.models import EmployeeProfile

User = get_user_model()


# =====================
# LOGIN
# =====================
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'ADMIN':
                return redirect('admin_dashboard')
            return redirect('employee_dashboard')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'accounts/login.html')


# =====================
# REGISTER
# =====================
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # validations
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        if User.objects.filter(employee_id=employee_id).exists():
            messages.error(request, "Employee ID already exists")
            return redirect('register')

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            employee_id=employee_id,
            password=password,
            role=role
        )

        # auto create employee profile
        EmployeeProfile.objects.create(
            user=user,
            designation="Employee",
            phone="",
            address="",
            salary=0
        )

        login(request, user)

        if role == 'ADMIN':
            return redirect('admin_dashboard')
        return redirect('employee_dashboard')

    return render(request, 'accounts/register.html')


# =====================
# LOGOUT
# =====================
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# =====================
# DASHBOARDS
# =====================
@login_required
def employee_dashboard(request):
    return render(request, 'employee/dashboard.html')


@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return redirect('employee_dashboard')
    return render(request, 'admin/dashboard.html')
