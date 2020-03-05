from django.shortcuts import render


def home(request):
    return render(request, 'constellations/index.html')


def about(request):
    return render(request, 'constellations/about.html')


def courses(request):
    return render(request, 'constellations/courses.html')
