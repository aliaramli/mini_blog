from django.contrib import admin
from .models import Post, CustomUser, Comment
from .form import CustomForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    form= CustomForm
    prepopulated_fields = {'slug': ('title',)}


class CustomUserAdmin(UserAdmin):
    fieldsets = (

        (                      # new fieldset added on to the bottom
            'User additional info',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
