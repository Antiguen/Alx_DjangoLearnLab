from relationship_app.models import Author, Book, Library, Librarian

# --- 1. SETUP SAMPLE DATA ---
# Create Author
author_orwell = Author.objects.create(name="George Orwell")

# Create Books (Many-to-One relationship with Author)
book_1984 = Book.objects.create(title="1984", author=author_orwell)
book_animal = Book.objects.create(title="Animal Farm", author=author_orwell)

# Create Library
main_library = Library.objects.create(name="Central Branch Library")

# Link Books to Library (Many-to-Many relationship)
main_library.books.add(book_1984, book_animal)

# Create Librarian (One-to-One relationship with Library)
librarian_smith = Librarian.objects.create(name="Jane Smith", library=main_library)


# --- 2. SAMPLE QUERIES (The required part of the task) ---

print("--- 1. Query all books by a specific author (ForeignKey) ---")
# Query all Books where the Author is George Orwell
orwell_books = Book.objects.filter(author__name='George Orwell')
for book in orwell_books:
    print(f"Book: {book.title}, Author: {book.author.name}")


print("\n--- 2. List all books in a library (ManyToManyField) ---")
# Retrieve the Library and then access its related books
library_books = Library.objects.get(name='Central Branch Library').books.all()
for book in library_books:
    print(f"Book in Library: {book.title}")


print("\n--- 3. Retrieve the librarian for a library (OneToOneField) ---")
# Retrieve the Library and then access the related Librarian
library = Library.objects.get(name='Central Branch Library')
librarian = library.librarian # Note the lowercase model name access
print(f"Librarian for {library.name}: {librarian.name}")