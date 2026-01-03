from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
