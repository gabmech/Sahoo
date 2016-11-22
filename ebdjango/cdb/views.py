from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from django.contrib.auth.models import User


def index(request):
    context = {}
    return render(request, 'index.html', context)

def signupPage(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/cdb/register_success')
		else:

			return HttpResponseRedirect('/cdb/register_invalid')
	args={}
	args.update(csrf(request))

	args['form']= MyRegistrationForm()

	return render_to_response('signup.html', args)
    #return render(request, 'signup.html', context)

def loggedinHome(request):
    #template = loader.get_template('index.html')
    context = {}
    return render(request, 'homeLoggedIn.html', context)


def guest_home(request):
	context = {}
	return render(request, 'guestHome.html', context)












# render login page
def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html', c)


# verify login information
def auth_view(request):
	username=request.POST.get('username', '')
	password=request.POST.get('password', '')
	user=auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/cdb/loggedin')

	else:
		return HttpResponseRedirect('/cdb/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',{ 'user_name':request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/cdb/')

# verify registration information and create user
def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/cdb/register_success')
		else:
			return HttpResponseRedirect('/cdb/register_invalid')
	args={}
	args.update(csrf(request))

	args['form']= MyRegistrationForm()
	
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')

def register_invalid(request):
	return render_to_response('invalid_register.html')

# render reset password page
def reset_password(request):
	c={}
        c.update(csrf(request))
	return render_to_response('reset_password.html', c)

# change user's password
def reset_password_form(request):
	username=request.POST.get('username', '')
	try:
		user = User.objects.get(username=username)
	except:
		return render_to_response('invalid_reset_password.html')
	password=request.POST.get('password', '')
	if password and user:
		user.set_password(password)
		user.save()
		return render_to_response('success_reset_password.html')
	else:
		return render_to_response('invalid_reset_password.html')

# render delete page
def delete_user(request):
        c={}
        c.update(csrf(request))
        return render_to_response('delete_user.html', c)	

# verify account to delete
def delete_auth(request):
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
        user=auth.authenticate(username=username, password=password)

        if user is not None:
                user.delete()
                return render_to_response('deleted_success.html')
        else:
                return render_to_response('deleted_invalid.html')
