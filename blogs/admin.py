from django.contrib import admin

from blogs.models import *


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    list_display = ['name', 'created_at']


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'position', 'created_at']
    list_filter = ['name', 'position', 'created_at']
    list_display = ['name', 'position', 'created_at']


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    list_display = ['name', 'created_at']


@admin.register(BlogModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    list_display = ['title', 'created_at']


