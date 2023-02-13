from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
from chatapp.models import Thread
from .forms import ThreadForm, UserForm
def home(request):
    if request.user.is_authenticated==False:
        return render(request, 'home.html')
    else:
        return redirect('chat')
        
@login_required      
def add_friend(request):
    if request.user.is_authenticated:
        user=request.user
        fm=ThreadForm(request.POST)
        if fm.is_valid():
            form=fm.save(commit=False)
            form.first_person=user
            first_person = form.first_person
            second_person = form.second_person
            lookup1 = Q(first_person=first_person) & Q(second_person=second_person)
            lookup2 = Q(first_person=second_person) & Q(second_person=first_person)
            lookup = Q(lookup1 | lookup2)
            qs = Thread.objects.filter(lookup)
            if qs.exists():
                messages.error(request, f'Friend {second_person} already exists.')
            else:
                if form.second_person!=user:
                    form.save()
                    return redirect('/')
                else:
                    messages.error(request, "Invalid")
                    return redirect('add_friend')
        else:
            return render(request, 'add_friend.html', {'fm':fm})

    return render(request, 'add_friend.html')
        
        
@login_required
def messages_page(request):
    Threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': Threads
    }
    return render(request, 'messages.html', context)

def signin(request):
    if request.user.is_authenticated==False:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')
            else:
                messages.error(request, "Username or Password Incorrect")
                return redirect('login')
        return render(request, 'login.html')
    else:
        return redirect('chat')

def signout(request):
    logout(request)
    return redirect('login')
    
def signup(request):
    if request.user.is_authenticated==False:
        fm=UserForm()
        if request.method=="POST":
            fm=UserForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Register Successful")
                return redirect("login")
            else:
                messages.error(request, "Username or Password Invaild")
                return redirect('register')
        return render(request, 'register.html', {'fm':fm})
    else:
        return redirect('chat')
