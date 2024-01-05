from django.urls import path
from core import views
urlpatterns = [
    path("", views.index, name='index'),
    path("category", views.category, name="category"),
    path("post/<str:slug>", views.view_post, name="post_view"),
    path("category/<str:slug>", views.cat_post, name="catPost"),
    path("login/", views.loginPage, name='login'),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.LogoutPage, name="logout"),
    path('profile/@<str:username>', views.profile, name="profile"),
    # path("profile", views.profile, name='profile'),
    path("profile-update", views.profileupdate, name='profile_update'),
]
