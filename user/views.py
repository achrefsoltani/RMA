from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

date = datetime.now

# Create your views here.

    

def profile(request):
    return render(request, 'user/profile.html', {'date':date})

def auth(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')    
        else:
            messages.success(request,("Il y a eu une erreur de connexion, réessayez s'il vous plaît..."))
            return redirect('signin')   
    else:   
        return render(request, 'user/auth.html', {
            'date':date

            })
def logout(request):
    logout(request)
    messages.success(request,("you were logout!"))  
    return redirect('home')          