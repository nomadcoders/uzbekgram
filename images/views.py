from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('you reached the index')


def explore(request):
    return HttpResponse('you reached the explore')


def profile(request):
    return HttpResponse('you reached the profile')
