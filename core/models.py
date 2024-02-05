from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# first last t email username password 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('Draft','Draft'),
        ('Publish','Publish')
    )

    featured_img = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, null=True)
    # content = models.TextField()
    content = RichTextField()
    slug = models.CharField(max_length=255, unique=True)
    status = models.CharField(choices=STATUS, max_length=150)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    location = models.CharField(max_length=255,blank=True)
    birth_date = models.DateField(blank=True, null=True)
    website = models.URLField(max_length=200,blank=True)
    facebook = models.URLField(max_length=200,blank=True)
    instagram = models.URLField(max_length=200,blank=True)
    linkedin = models.URLField(max_length=200,blank=True)
    github = models.URLField(max_length=200,blank=True)
    youtube = models.URLField(max_length=200,blank=True)
    profile_image = models.ImageField(blank=True,null=True,default="profile/default.png")

    def __str__(self):
        return str(self.user)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username 