from django.contrib import admin
from .models import (
    Category,
    Tag,
    Post
)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "is_published")

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
