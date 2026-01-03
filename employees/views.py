from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EmployeeProfile


@login_required
def profile_view(request):
    # ✅ SAFE: auto-create profile if missing
    profile, created = EmployeeProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "designation": "Employee",
            "phone": "",
            "address": "",
            "salary": 0
        }
    )

    if request.method == 'POST':
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        return redirect('profile')

    return render(request, 'employee/profile.html', {'profile': profile})
