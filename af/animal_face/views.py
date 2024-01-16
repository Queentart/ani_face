from django.shortcuts import render
# from django.http import HttpResponse


def main(request):
    return render(request, 'main.html')

def welcome(request):
    return render(request, 'welcome.html')

# Create your views here.
