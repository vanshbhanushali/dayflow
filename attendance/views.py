from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from .models import Attendance
from django.shortcuts import render

@login_required
def check_in(request):
    Attendance.objects.get_or_create(
        user=request.user,
        date=date.today(),
        defaults={
            'check_in': datetime.now().time(),
            'status': 'Present'
        }
    )
    return redirect('employee_dashboard')


@login_required
def check_out(request):
    attendance = Attendance.objects.filter(
        user=request.user,
        date=date.today()
    ).first()

    if attendance:
        attendance.check_out = datetime.now().time()
        attendance.save()

    return redirect('employee_dashboard')



@login_required
def attendance_history(request):
    records = Attendance.objects.filter(user=request.user).order_by('-date')
    return render(request, 'attendance/history.html', {'records': records})