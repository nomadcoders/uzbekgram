from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image
from django.contrib.auth.models import User


def index(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
        users = User.objects.all()
        return render(request, "feed.html", context={
            'potatos': all_images,
            'users': users
        })
    else:
        return render(request, "login.html")


def explore(request):
    user = request.user
    if user.is_authenticated:
        users = User.objects.all()
        return render(request, "explore.html", context={
            'users': users
        })
    else:
        return render(request, "login.html")


def profile(request):
    return HttpResponse('you reached the profile')
