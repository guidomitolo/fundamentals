from django.shortcuts import render

# Create your views here.

def home(requests):
    context = {'title': 'home'}
    return render(requests, 'main/home.html', context)
