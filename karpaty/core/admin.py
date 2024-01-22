from django.contrib import admin
from .models import Post, Categories



@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("name",)}
