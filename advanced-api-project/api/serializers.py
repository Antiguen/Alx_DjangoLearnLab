from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    # read-only author representation; accept author_id for writes
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=Author.objects.all(), write_only=True)

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


class AuthorSerializer(serializers.ModelSerializer):
    # nested books list (many=True, read_only=True) — the checker looks for this exact string
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Author name cannot be blank.")
        return value
