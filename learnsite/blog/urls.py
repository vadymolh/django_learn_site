from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.blog_main), # domen.com/blog/
    path('<slug>/', views.slug_process),
]

