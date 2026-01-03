from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('attendance/', include('attendance.urls')),
    path('leaves/', include('leaves.urls')),
    path('employee/', include('employees.urls')),

]
