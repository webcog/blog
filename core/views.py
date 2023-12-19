from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from core.models import Category, Post
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

def index(request):
    category = Category.objects.all().order_by("-id")
    post = Post.objects.all().order_by("-id")

    context = {
        'category':category,
        'post':post,
    }

    return render(request, 'index.html', context)

def category(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request, 'category.html',context)


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post":post
    }
    return render(request, "single.html",context)

def cat_post(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)

    context = {
        'category':category,
        'posts':posts
    }
    return render(request, 'cat_post.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('index')
            
        else:
            messages.error(request, "Wrong Credentials Insert")
        
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        
        a = "12345678"
        
        if pass1 != pass2:
            messages.error(request, "Password did Not Match!")
        
        

        elif len(pass1)  <= len(a) and len(pass2)  <= len(a):
            messages.error(request, "Your Password length is smaller than 8")
    
        else:
            try:
                my_user = User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                messages.error(request,"Your Username Already Exist")
    return render(request, 'signup.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')