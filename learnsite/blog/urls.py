from django.urls import path, include, re_path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path(r'', cache_page(60*30)(views.PostListMain.as_view()) ), # domen.com/blog/
    path('register/', views.UserRegistration.as_view()),
    path('logout/', views.logout_request),
    path('login/', views.login_request),
    path('search_post/', views.search_post, name="search"),
    path('profile/', views.profile, name='user_profile'),
    path('profile/<username>', views.look_profile, name="look_profile"),
    path('post_like/<int:post_id>', views.like_post, name="like_post"),
    path('post/<slug:slug>/',cache_page(60*30)(views.ShowPost.as_view()) , name="post_url"),
    path('<slug>/', views.slug_process),
]

