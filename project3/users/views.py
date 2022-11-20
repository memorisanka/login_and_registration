from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages


def home(request):
    return render(request, 'users/home.html', {'title': 'Welcome'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account has been created. Welcome, {username}!")
        #     redirect do strony po zalogowaniu
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html', {})

