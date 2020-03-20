from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MailingList
from .forms import MailingListForm
from accounts.models import Profile
from django.views.generic import ListView
from events.models import EventType


def home(request):
    profile = Profile.objects.all()
    return render(request, 'constellations/index.html')
    '''{'profile': profile}'''


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


class student_testimonials(ListView):
    model = Profile
    template_name = 'constellations/testimonials.html'
    context_object_name = 'profiles'
    paginate_by = 5
