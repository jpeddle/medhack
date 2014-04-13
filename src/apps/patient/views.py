from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def upcoming_appointments(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/upcoming_appointments.html',
        dictionary={
            'patients': patients,
            'page_name': 'upcoming'
        }
    )

@login_required
def family_members(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/family.html',
        dictionary={
            'patients': patients,
            'page_name': 'family'
        }
    )

@login_required
def billing_information(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/billing.html',
        dictionary={
            'patients': patients,
            'page_name': 'billing'
        }
    )

@login_required
def insurance_information(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/insurance.html',
        dictionary={
            'patients': patients,
            'page_name': 'insurance'
        }
    )

