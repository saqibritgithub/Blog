from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import logout
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, 'users/sign_up.html', {'form': form})
    else:
        
        form = SignUpForm()
        return render(request, 'users/sign_up.html', {'form': form})
    
def  logout_Fun(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
    return render(request,'users/profile.html')