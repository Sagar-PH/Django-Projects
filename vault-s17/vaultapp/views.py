
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
from .models import Vault
from .forms import VaultForm, RegisterForm
from django.conf import settings
import os
from django.http import Http404, HttpResponse

def home(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method=="POST":
            fm=VaultForm(request.POST, request.FILES)
            if fm.is_valid():
                form=fm.save(commit=False)
                form.user=user
                fm.save()
                return redirect('/')
        else:
            fm=VaultForm()
            return render(request, 'home.html', {'vault':Vault.objects.filter(user=user), 'fm':fm})
    return render(request, 'home.html')

@login_required
def delete(request, pk):
    user=request.user
    todo=Vault.objects.get(id=pk)
    if user==todo.user:
        todo.delete()
        return redirect('home')
    else:
        return redirect('/')

def download(request, path):
    file_path=os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

def signin(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There was error.'))
            return redirect('login')

    else:
        return render(request,'login.html')

def signout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.success(request, ('There was error.'))
            return redirect('register')
    else:
        form= RegisterForm()
    return render(request, 'register.html', {'form':form})