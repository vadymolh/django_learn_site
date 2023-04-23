from django.db import models
from django.contrib import admin
from .models import Post, Comment, Category
#from tinymce.widgets import TinyMCE
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'created_at', 'img', 'category', 'post_slug')
    #formfield_overrides = { 
    #                        models.TextField: {'widget': TinyMCE()}
    #                      }


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)