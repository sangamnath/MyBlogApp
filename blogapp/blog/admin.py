from django.contrib import admin
from .models import Category, Comment, Post, Profile
from chat.models import Message
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Message)