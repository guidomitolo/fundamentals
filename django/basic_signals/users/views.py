from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡You have registered!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(
        request, 
        'users/register.html', 
        {
            'title': 'register',
            'form': form
        }
    )