from django.db import models
from django.conf import settings
class Author(models.Model):
    """Simple Author model."""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model with a ForeignKey to Author (Many-to-One relationship).
    Multiple books can have one author.
    """
    title = models.CharField(max_length=200)
    
    # ForeignKey: One Author can write many Books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    """
    Library model with a ManyToManyField to Book (Many-to-Many relationship).
    A Library can hold many Books, and a Book can be in many Libraries.
    """
    name = models.CharField(max_length=100)
    
    # ManyToManyField: Links Library to Book.
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    """
    Librarian model with a OneToOneField to Library (One-to-One relationship).
    Each Librarian is assigned to exactly one Library, and vice versa.
    """
    name = models.CharField(max_length=100)
    
    # OneToOneField: Links Librarian to Library.
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name