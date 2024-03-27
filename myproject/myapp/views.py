from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . forms import MyRegFrm, MyLogFrm
from . models import  Product

# Create your views here.

def about(request):
    return render(request, 'myapp/about.html')

def client(request):
    return render(request, 'myapp/client.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def index(request):
    products=Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})

def products(request):
    return render(request, 'myapp/products.html')

def userReg(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration is successful')
            except Exception :
                messages.error(request, 'Registration is unsuccessful')
    else:
        form=MyRegFrm()
    return render(request, 'myapp/reg.html',{'form':form})


def userLog(request):
    if request.POST:
        form=MyLogFrm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')

    else:
        form=MyLogFrm()
    return render(request, 'myapp/log.html', {'form':form})

def userLogout(request):
    logout(request)
    return redirect('/login/')
 

 