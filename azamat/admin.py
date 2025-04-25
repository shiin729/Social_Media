from django.contrib import admin
from .models import Post, Profile, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Profile)
admin.site.register(Comment)

# Register your models here.
