from django.shortcuts import render,redirect
from store.forms.authforms import CustomerCreationForm ,CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser
from store.models import Tshirt
from math import floor

def home(request):
    tshirts=Tshirt.objects.all()
    context={ "tshirts" : tshirts}
    

    return render(request,template_name="store/home.html",context=context)

def show_product(request, id):
    tshirt=Tshirt.objects.get(pk=id)
    return render(request,template_name="store/products_details.html", context={"tshirt": tshirt})

def cart(request):
    return render(request,template_name="store/cart.html")

 


def logout(request):
    request.session.clear()
    return render(request,template_name="store/home.html")


def login(request):
    if request.method=="GET":
        form=CustomerAuthForm()
        return render(request,template_name="store/login.html", context={"form":form})

    else:
        form =CustomerAuthForm(data= request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user= authenticate(username= username,password=password)
            if user:
                loginUser(request,user)
                return redirect("homepage")

        else:
            return render(request,template_name="store/login.html", context={"form":form})


def oders(request):
    return render(request,template_name="store/oders.html")


def signup(request):
    if request.method=="GET":

        form=CustomerCreationForm()
        
        context={
            "form": form
        }
        return render(request,template_name="store/signup.html", context=context)
    else:
        form= CustomerCreationForm(request.POST)
        #print(form.is_valid())
        #print(form.errors)
        if form.is_valid():
            user=form.save()
            user.email=user.username
            user.save()
            return render(request,template_name="store/login.html")

        context={
            "form": form
        }
        return render(request,template_name="store/signup.html", context=context)