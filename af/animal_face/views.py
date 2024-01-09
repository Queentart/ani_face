from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("작동성공")

# Create your views here.
