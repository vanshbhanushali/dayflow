from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest


@login_required
def apply_leave(request):
    if request.method == 'POST':
        LeaveRequest.objects.create(
            user=request.user,
            leave_type=request.POST.get('leave_type'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            reason=request.POST.get('reason'),
        )
        return redirect('employee_dashboard')

    return render(request, 'leaves/apply.html')


@login_required
def manage_leaves(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'leaves/manage.html', {'leaves': leaves})


@login_required
def approve_leave(request, id):
    leave = LeaveRequest.objects.get(id=id)
    leave.status = 'Approved'
    leave.save()
    return redirect('manage_leaves')


@login_required
def reject_leave(request, id):
    leave = LeaveRequest.objects.get(id=id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('manage_leaves')
