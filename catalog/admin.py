from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import User, Author, Tag, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "owner"]
    list_filter = ["tag", "author", "owner", "borrower"]
    search_fields = ["title", ]


admin.site.register(User)
admin.site.register(Author)
admin.site.register(Tag)
