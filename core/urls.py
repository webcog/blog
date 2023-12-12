from django.urls import path
from core import views
urlpatterns = [
    path("", views.index, name='index'),
    path("category", views.category, name="category"),
    path("post/<str:slug>", views.view_post, name="post_view"),
    path("category/<int:id>", views.cat_post, name="catPost")
]
