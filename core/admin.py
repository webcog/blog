from django.contrib import admin
from core.models import Category,Post


# Register your models here.

class AdminPost(admin.ModelAdmin):
    model=Post
    list_display=("title","author","category","status","date",'slug')
    

admin.site.register(Category)
admin.site.register(Post, AdminPost)