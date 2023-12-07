from django.shortcuts import render
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