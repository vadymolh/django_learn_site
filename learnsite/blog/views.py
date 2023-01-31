from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.



def blog_main(request, *args):
    page = request.GET.get('page')
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    try:
        data_page = paginator.page(page)
    except PageNotAnInteger:
        data_page = paginator.page(1)
    except EmptyPage:
        data_page = paginator.page(paginator.num_pages)
    data_dict  ={
        "posts": data_page
    }
    return render(request, 'blog_main.html', data_dict)

def search_post(request):
    """Functionality for navbar 
    to process search form"""
    posts=None
    if request.method=="POST":
        text = request.POST.get("searchpost")
        posts = Post.objects.filter(title__icontains=text)
    data_dict = {"posts": posts}
    return render(request, 'blog_main.html', data_dict )



def slug_process(request, slug):
    post_slugs = [ p.post_slug for p in Post.objects.all()]
    if slug in post_slugs:
        post = Post.objects.get(post_slug = slug)
        if request.user.is_authenticated:
            if not post.views_number.filter(id=request.user.id).exists():
                post.views_number.add(request.user)
        views = post.get_views_number()        
        data_dict = { 'post': post,
                      'views_num': views }
        return render(request, 'post_view.html', data_dict)

def register(request):
    # POST incomig
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get("username")
            messages.success(request, f"Створено новий акаунт: {username}")
            return redirect("/")
        else:
            print("ERROR DURING REGISTRATION!+")
            for msg in form.error_messages:
                messages.error(request, f"{msg}")
            return render(request, 'register.html', {'form': form})
    # GET incoming
    data_dict = {'form': UserCreationForm}
    return render(request, 'register.html', data_dict)

def logout_request(request):
    logout(request)
    messages.info(request ,"Ви вийшли з акаунту!")
    return redirect("/")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Ви упішно залогінились")
                return redirect("/")
            else:
                for msg in form.error_messages:
                    messages.error(request, f"Помилка, неправильний {msg}")
                return redirect("/login")
    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})