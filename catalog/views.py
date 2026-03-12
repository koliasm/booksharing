from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Book, Author, Tag
from django.contrib.auth import get_user_model


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_tags = Tag.objects.count()
    num_users = get_user_model().objects.count()

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_tags": num_tags,
        "num_users": num_users,
    }
    return render(request, "catalog\index.html", context=context)
