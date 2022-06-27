from django.contrib import admin
from .models import Blog, Comment, Popular
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['id','author','title','description','created_on', 'images']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','comment','name','email','body']
    

@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    list_display=['id','author','title','description','created_on', 'images', 'is_popular']