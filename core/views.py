from django.shortcuts import render, get_object_or_404
from core.models import Category, Post
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


def login(request):
    return render(request, 'login.html')