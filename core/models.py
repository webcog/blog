from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('Draft','Draft'),
        ('Publish','Publish')
    )

    featured_img = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, null=True)
    # content = models.TextField()
    content = RichTextField()
    slug = models.CharField(max_length=255, unique=True)
    status = models.CharField(choices=STATUS, max_length=150)

    def __str__(self):
        return self.title