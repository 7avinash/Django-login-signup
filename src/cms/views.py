from django.shortcuts import render
from .forms import UserDetailForm, UserCreateForm, LogInForm
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def SignUp(request):
	form = UserCreateForm(request.POST or None)
	form1 = UserDetailForm(request.POST or None)

	if form.is_valid() and form1.is_valid():
		instance = form.save()
		extradetails = form1.save(commit = False)
		extradetails.user = instance
		extradetails.save()
		messages.success(request, "You have successfully registered")
		return HttpResponseRedirect("/")

	context = {
		'form':form,
		'form1':form1
	}
	context.update(csrf(request))

	return render(request, 'signup.html', context)

def LogIn(request):
	form = LogInForm(request.POST or None)

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)

				return HttpResponseRedirect("/home/")

		else:
			messages.error(request, "Incorect Username or Password")

	context = {
		'form':form,
	}

	context.update(csrf(request))
	return render(request, 'login.html', context)

@login_required
def Home(request):
	user = request.user
	phone = UserDetail.objects.filter(user__username = user)
	print phone
	context = {
		'phone':phone
	}

	if request.method == 'POST':
		if request.POST.get('logout') == 'logout':
			logout(request)
			return HttpResponseRedirect("/")

	return render(request, 'home.html', context)










	



