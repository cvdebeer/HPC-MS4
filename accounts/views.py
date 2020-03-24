from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import (ProfileUpdateForm, StudentRegistrationForm,
                    StudentUpdateForm)
from .models import Profile, User


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = username
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_update(request):
    user = User.objects.all()
    profile = Profile.objects.all()
    if request.method == 'POST':
        su_form = StudentUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if su_form.is_valid() and pu_form.is_valid():
            su_form.save()
            pu_form.save()
            messages.success(
                request, f'Your profile has been updated')
            return redirect('profile')
    else:
        su_form = StudentUpdateForm(instance=request.user)
        pu_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'su_form': su_form,
        'pu_form': pu_form
    }
    return render(request, 'accounts/profile_update.html', context)
