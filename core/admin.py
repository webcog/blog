from django.contrib import admin
from core.models import Category,Post,Profile, Comment


# Register your models here.

class AdminPost(admin.ModelAdmin):
    model=Post
    list_display=("title","author","category","status","date",'id')
    prepopulated_fields = {'slug':("title","author","category")}

class AdminCategory(admin.ModelAdmin):
    list_display=('name',"slug","date")  
    prepopulated_fields = {'slug':("name",)}
    
admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)

admin.site.register(Profile)

admin.site.register(Comment)