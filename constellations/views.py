from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MailingList
from .forms import MailingListForm
from accounts.models import Profile
from events.models import EventType


def home(request):
    profile = Profile.objects.all()
    return render(request, 'constellations/index.html', {'profile': profile})


def about(request):
    return render(request, 'constellations/about.html')


def courses(request):
    course = EventType.objects.all()
    return render(request, 'constellations/courses.html', {'course': course})


def mailing_list(request):

    if request.method == 'POST':
        form = MailingListForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('fullname')
            messages.success(
                request, f'Your have been added to our mailing list')
        return redirect('home-page')

    else:
        form = MailingListForm()

    return render(request, 'constellations/mailing_list.html', {'form': form})


def student_testimonials(request):
    profile = Profile.objects.all()
    return render(request, 'constellations/testimonials.html', {'profile': profile})
