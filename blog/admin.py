from django.contrib import admin
from .models import Post
from .form import CustomForm

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    form= CustomForm
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
