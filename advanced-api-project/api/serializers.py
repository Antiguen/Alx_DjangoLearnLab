from rest_framework import serializers
from .models import Author, Book
import datetime


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Author name cannot be blank.")
        return value


class BookSerializer(serializers.ModelSerializer):
    # show nested author on read and accept author_id on write
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", queryset=Author.objects.all(), write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "author_id",
            "publication_year",
            "description",
        ]

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value

    def validate_publication_year(self, value):
        if value is None:
            return value
        current_year = datetime.date.today().year
        if value < 0 or value > current_year:
            raise serializers.ValidationError("Enter a valid publication year.")
        return value
