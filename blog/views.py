from django.shortcuts import render
from .models import blog
from .forms import createpostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def test(request,slu):
    data=blog.objects.get(id=slu)
    totle=blog.objects.all()
    return render(request,'blog.html',{'d':data,'t':totle})



def createpostFor(request):
    new=createpostForm(request.POST,request.FILES)
    obj=blog()
    if new.is_valid():
        obj.title=new.cleaned_data['title']
        obj.img = new.cleaned_data['img']
        obj.detiles = new.cleaned_data['detiles']
        obj.save()
    return render(request, 'ceartposts.html', {'username':new})




# Create your views here.
