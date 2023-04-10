from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm, FrontEndForm
from django.contrib import auth, messages
from django.contrib.auth import authenticate, logout, get_user_model

from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from .models import Items, FrontEnd
# Create your views here.

def frontend_detail(request, frontend_id):
    frontends = get_object_or_404(FrontEnd, pk=frontend_id)
    context = {'frontends': frontends}
    return render(request, 'accounts1/frontend_detail.html', context)
def frontend_display(request, frontend_id):
    frontends = get_object_or_404(FrontEnd, pk=frontend_id)
    context = {'frontends': frontends}
    return render(request, 'accounts1/frontend_display.html', context)
def home(request):
	return render(request, 'dashboard.html')

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Account created successfully!')
			user=form.save()
			subject='Thanks for register'
			message='Hey Welcome to my website.'
			to=user.email
			send_mail(
				subject,
				message,
				'sagargowda9128@gmail.com',
				[to],

				)
	else:
		form = RegisterForm()
	return render(request, 'accounts1/register.html', {'form':form})

def log_in(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = LoginForm(request=request, data=request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				upass = form.cleaned_data['password']
				user = authenticate(username=uname, password=upass)
				if user is not None:
					auth.login(request, user)
					messages.success(request,'Logged in successfully!')
					return redirect('/base/')
			else:
				messages.info(request,'Username or Password incorrect!')
		else:
			form = LoginForm()
		return render(request, 'accounts1/login.html', {'form':form})
	else:
		return redirect('/base/')

@login_required
def base(request):
	item = Items.objects.all()
	frontends = FrontEnd.objects.filter(user=request.user)
	context = {'name': request.user, 'item': item, 'frontends': frontends}
	return render(request, 'accounts1/base.html', context)

def cardform(request):
    if request.user.is_authenticated:
        user=request.user
        fm=FrontEndForm(request.POST)
        if fm.is_valid():
            form=fm.save(commit=False)
            form.user=user
            form.save()
            messages.success(request, ('Added'))
            return redirect('base')
        else:
            return render(request, 'accounts1/cardform.html', {'fm':fm})

    return render(request, 'dashboard.html')
@login_required
def edit(request, pk):
    user=request.user
    frontend=FrontEnd.objects.get(id=pk)
    if user==frontend.user:
        fm=FrontEndForm(instance=frontend)
        if request.method=='POST':
            fm=FrontEndForm(request.POST, instance=frontend)
            if fm.is_valid():
                form=fm.save(commit=False)
                form.user=user
                fm.save()
                return redirect('base')

        return render(request, 'accounts1/edit.html', {'fm':fm})
    else:
        return redirect('base')

@login_required
def delete(request, pk):
    user=request.user
    frontend=FrontEnd.objects.get(id=pk)
    if user==frontend.user:
        frontend.delete()
        return redirect('base')
    else:
        return redirect('base')
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,'Updated successfully!')
		else:
			messages.error(request, 'Invalid!')
			return redirect('/profile/')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'accounts1/profile.html', context)


@login_required
def log_out(request):
	logout(request)
	return redirect('/login/')

User = get_user_model()

class UserDelete(DeleteView):
	model = User
	success_url = reverse_lazy('')
	template_name = 'delete_account.html'

def search(request):
	if request.method == "GET":
		search = request.GET.get('search')
		post = Article.objects.all().filter(title=search)
		return render(request, 'articles/articles_list.html', {'post':post})