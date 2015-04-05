from django.contrib import admin

from blog.models import Post

# Register your models here.

admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')
