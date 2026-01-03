from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_leave, name='apply_leave'),
    path('manage/', views.manage_leaves, name='manage_leaves'),
    path('approve/<int:id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:id>/', views.reject_leave, name='reject_leave'),
]
