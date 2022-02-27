from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('run_stats:index'))


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('run_stats:index'))

    context = {'form': form}

    return render(request, 'users/register.html', context)
