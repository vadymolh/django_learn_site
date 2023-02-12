from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.blog_main), # domen.com/blog/
    path('register/', views.register),
    path('logout/', views.logout_request),
    path('login/', views.login_request),
    path('search_post/', views.search_post, name="search"),
    path('profile/', views.profile, name='user_profile'),
    path('profile/<username>', views.look_profile, name="look_profile"),
    path('post_like/<int:post_id>', views.like_post, name="like_post"),
    path('<slug>/', views.slug_process),
]

