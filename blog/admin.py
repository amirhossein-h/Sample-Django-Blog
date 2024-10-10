from django.contrib import admin
from .models import Index, Post, Comment, General, TableData

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ["title", "short_text"]

    def short_text(self, obj):
        if obj.text:
            return obj.text[:40]
        else:
            return "__"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "summary"]

    def title(self, obj):
        return obj.index.title

    def summary(self, obj):
        if obj.summary_text:
            return obj.summary_text[:40]
        else:
            return "__"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user_name", "post_name", "datetime_created", "short_text"]

    def user_name(self, obj):
        return obj.user.username

    def post_name(self, obj):
        if obj.post.title:
            return obj.post.title
        else:
            return "__"

    def short_text(self, obj):
        if obj.text:
            return obj.text[:30]
        else:
            return "__"


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ["content_for", "title", "summary"]

    def summary(self, obj):
        if obj.summary_text:
            return obj.summary_text[:30]
        else:
            return "__"


@admin.register(TableData)
class TableDataAdmin(admin.ModelAdmin):
    list_display = ["content_for", "table_name", "related_to_section"]

    def related_to_section(self, obj):
        if obj.related_to:
            return obj.related_to
        else:
            return "__"