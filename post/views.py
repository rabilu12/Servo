from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import signform
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from django.forms import inlineformset_factory
import bcrypt


def signup(request):
    form = signform()
    context = {'form':form}
    if request.method == 'POST':
        form = signform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('YOUR REGISTRATION IS SUCCESSFUL')
    return render(request, 'post/signup.html', context)
       

#Create your views here.
def index(request):
    print ('Hope its working')
    return render(request, 'post/index.html')

def validate(request):
    # print 'ready to validate!'
    if request.method=='POST':
        # print 'POSTED!'
        userobject = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'confirm': request.POST['confirm']
        }
        errors = User.objects.validate(userobject)
        if errors:
            # print errors
            for each in errors:
                messages.error(request, each)
        else:
            # print 'things!'
            newuser = User.objects.create(
                first_name=userobject['first_name'],
                last_name=userobject['last_name'],
                email=userobject['email'],
                password=(
                    bcrypt.hashpw(userobject['password'].encode(),
                                  bcrypt.gensalt())
                )
            )
            request.session['id'] = newuser.id
            return redirect('/register')
    return redirect('/')

def register(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'first_name': user.first_name,
        'achievement': 'registered'
    }
    return render(request, 'post/success.html', context)

def verify(request):
    if request.method=='POST':
        logobject = {
            'email': request.POST['log_email'],
            'password': request.POST['log_password']
        }
        verification = User.objects.verify(logobject)
        if verification['errors']:
            for each in verification['errors']:
                messages.error(request, each)
        else:
            request.session['id'] = verification['id']
            return redirect('/login')
    return redirect('/')

def login(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'first_name': user.first_name,
        'achievement': 'logged in'
    }
    return render(request, 'post/success.html', context)
