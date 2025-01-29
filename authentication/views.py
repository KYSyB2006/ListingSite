from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserAuthenticationForm
from listing.models import Etudiant
# Create your views here.

def loginSite(request, msg=None):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.role == 'PROFESSEUR':
                    login(request, user)
                    return redirect("EnseignantSpace")
                elif user.role== 'ETUDIANT':
                    login(request, user)
                    return redirect('EtudiantSpace')
                else:
                    return redirect('admin:index')

    else:
        form = UserAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logoutSite(request):
    logout(request)
    return render(request,'logout.html')