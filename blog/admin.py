from django.contrib import admin
from .models import BlogContent
# Register your models here.

class For_blog_content(admin.ModelAdmin):
    list_display = ['header','content','image']

admin.site.register(BlogContent,For_blog_content)

