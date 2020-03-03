from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = username
            messages.success(request, f'Account created for {username}!')
            return redirect('register')

    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
