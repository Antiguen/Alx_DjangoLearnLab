from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view to list all Book objects.
    - queryset: specifies which data to retrieve (all books).
    - serializer_class: specifies how to convert the data into JSON.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer