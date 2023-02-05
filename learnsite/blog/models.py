from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='blog/static/img/profiles',
                               default = 'blog/static/img/profiles/default.png',
                               verbose_name = 'Фото профілю')
    about = models.TextField(max_length=500,
                             verbose_name = 'Про себе',
                             blank=True)
    def save(self,*agr, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height>120 or img.width>120:
            img.thumbnail((120, 120))
            img.save(self.avatar.path)
    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    post_slug = models.CharField(max_length=80, default="default_post")
    img = models.ImageField(default = 'blog/static/img/default.png',
                            upload_to='blog/static/img',
                            height_field=None,
                            width_field=None,
                            max_length=200,
                            verbose_name="Картинка для поста")
    views_number = models.ManyToManyField(User, related_name="views_rating", blank=True)
    def get_views_number(self):
        return self.views_number.count()
    def save(self, *agr, **kwargs):
        super().save()
        img = Image.open(self.img.path)
        if img.height>720 or img.width>1080:
            img.thumbnail((720, 1080))
            img.save(self.img.path)
    def __str__(self):
        return self.title
