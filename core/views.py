from django.shortcuts import render
from core.models import Category, Post
# Create your views here.

def index(request):
    return render(request, 'index.html')

def category(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request, 'category.html',context)