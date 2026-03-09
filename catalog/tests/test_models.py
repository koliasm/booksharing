from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.models import Author, Tag, Book

class ModelTestStr(TestCase):
    def test_user_str(self):
        user = get_user_model().objects.create_user(
            username="username",
            password="password",
            first_name="Test_first",
            last_name="Test_last",
            telegram_tag="test_tag",
        )
        self.assertEqual(
            str(user),
            f"{user.first_name} {user.last_name} "
            f"@{user.telegram_tag}")

    def test_author_str(self):
        author = Author.objects.create(
            first_name="Test_first",
            last_name="Test_last",
        )
        self.assertEqual(
            str(author),
            f"{author.first_name} {author.last_name}"
        )

    def test_tag_str(self):
        tag = Tag.objects.create(
            name="Fiction",
        )
        self.assertEqual(
            str(tag),
            f"{tag.name}"
        )


    def test_book_str(self):
        owner = get_user_model().objects.create_user(
            username="owner",
            password="password1",
            first_name="Owner_first",
            last_name="Owner_last",
            telegram_tag="Owner_tag",
        )
        borrower = get_user_model().objects.create_user(
            username="borrower",
            password="password2",
            first_name="Borrower_first",
            last_name="Borrower_last",
            telegram_tag="Borrower_tag",
        )
        author = Author.objects.create(
            first_name="Author_first",
            last_name="Author_last",
        )
        tag = Tag.objects.create(
            name="fiction",
        )
        book = Book.objects.create(
            title="Harry Potter",
            owner=owner,
            borrower=borrower,
        )
        book.author.add(author)
        book.tag.add(tag)

        self.assertEqual(
            str(book),
            f"{book.title} - {book.author}"
        )
