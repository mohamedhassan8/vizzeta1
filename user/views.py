from django.shortcuts import render
from .models import profiel ,pest_profiel
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import createuser ,ProfileUpdateForm
from django.db.models import Q


from django.contrib.auth.forms import UserCreationForm

def passb1(request):
    data = profiel.objects.all()
    pest=pest_profiel.objects.all()
    return render(request,'indx.html',{'data':data,'pest':pest})
def profel(request,slug):
    data=profiel.objects.get(slug=slug)

    return render(request,'profiel.html',{'data':data})

def log (request):
    return render(request,'login.html',)
def backlog (request):
    n= request.POST['name']
    p=request.POST['password']
    lo=authenticate(request,username=n,password=p)
    if lo is not None:
        login(request,lo)
        return redirect('pass1')
    return render(request,'login.html',)
@ login_required(login_url='log')
def my_profile(request):
    return render(request,'myprofil.html',)

def crea(request):
    return render(request,'singup2.html',)
def backcreate(request):

    nam=User.objects.create_user(request.POST['username'] ,request.POST['emil'],request.POST['password'])
    nam.first_name=request.POST['first_name']
    nam.last_name=request.POST['lastname']
    nam.save()
    return redirect('pass1')


login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profiel)
        if p_form.is_valid() :
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
    context={'p_form': p_form}
    return render(request, 'profile.html',context )

def logout1(request):
    logout(request)
    return redirect('pass1')



def search(request):
    sear = request.POST['search']
    data = profiel.objects.filter(who_i=sear)

    return render(request, 'bak_search.html', {'data': data})


# Create your views here.
