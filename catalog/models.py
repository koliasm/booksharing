from django.contrib.auth.models import AbstractUser
from django.db import models

from booksharing.settings import AUTH_USER_MODEL


class User(AbstractUser):
    telegram_tag = models.CharField(max_length=255)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} "
                f"@{self.telegram_tag}")


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name="books")
    tag = models.ManyToManyField(Tag, related_name="books")
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_books",
    )
    borrower = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="borrowed_books",
    )

    def __str__(self):
        return f"{self.title} - {self.author}"
