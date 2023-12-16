from django.urls import path
from core import views
urlpatterns = [
    path("", views.index, name='index'),
    path("category", views.category, name="category"),
    path("post/<str:slug>", views.view_post, name="post_view"),
    path("category/<str:slug>", views.cat_post, name="catPost"),
    path("login/", views.login, name='login'),
    path('signup/', views.signup, name="signup")
]
