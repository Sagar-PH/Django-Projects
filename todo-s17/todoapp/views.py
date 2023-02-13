
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
from .models import Todo
from .forms import TodoForm, RegisterForm

def home(request):
    if request.user.is_authenticated:
        user=request.user
        fm=TodoForm(request.POST)
        if fm.is_valid():
            form=fm.save(commit=False)
            form.user=user
            form.save()
            messages.success(request, ('Added'))
            return redirect('/')
        else:
            todo=Todo.objects.filter(user=user)
            return render(request, 'todo/home.html', {'todo':todo, 'fm':fm})

    return render(request, 'todo/home.html')

@login_required
def edit(request, pk):
    user=request.user
    todo=Todo.objects.get(id=pk)
    if user==todo.user:
        fm=TodoForm(instance=todo)
        if request.method=='POST':
            fm=TodoForm(request.POST, instance=todo)
            if fm.is_valid():
                form=fm.save(commit=False)
                form.user=user
                fm.save()
                return redirect('/')

        return render(request, 'todo/edit.html', {'fm':fm})
    else:
        return redirect('/')

@login_required
def delete(request, pk):
    user=request.user
    todo=Todo.objects.get(id=pk)
    if user==todo.user:
        todo.delete()
        return redirect('home')
    else:
        return redirect('/')

def signin(request):
    if request.user.is_authenticated==True:
        return redirect('home')
    else:
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
            return render(request,'todo/login.html')

def signout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.user.is_authenticated==True:
        return redirect('home')
    else:
        form= RegisterForm()
        if request.method=="POST":
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.success(request, ('There was error.'))
                return redirect('register')
        return render(request, 'todo/register.html', {'form':form})

@login_required
def changepass(request):
    fm=PasswordChangeForm(request.user)
    if request.method=="POST":
        fm=PasswordChangeForm(request.user, request.POST)
        if fm.is_valid():
            user = fm.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Password Changed Successfully'))
            return redirect('home')
        else:
            messages.error(request, ('Password Change Failed'))
            return redirect('changepass')
    return render(request, "todo/changepass.html", {'fm':fm})
