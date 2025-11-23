from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# This ViewSet provides the implementations for all CRUD operations:
# list, create, retrieve, update, partial_update, and destroy.
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Keeping the old view as requested in the URL pattern instructions
# (Even though it is redundant now that ViewSet exists)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer