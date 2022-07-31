from django.contrib import admin

from .models import Author, Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ["title", "tag", "date"]
    list_display = ["title", "date", "author"]
    prepopulated_fields = {"slug":("title",)}

class CommentAdmmin(admin.ModelAdmin):
    list_display = ["user_name", "post"]
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmmin)