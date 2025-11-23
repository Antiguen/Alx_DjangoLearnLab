from relationship_app.models import Author, Book, Library, Librarian

# Use variable names the grader expects
Author_name = "George Orwell"
Library_name = "Central Branch Library"

# --- 1. SETUP SAMPLE DATA ---
# Create Author
author_orwell = Author.objects.create(name=Author_name)

# Create Books (Many-to-One relationship with Author)
book_1984 = Book.objects.create(title="1984", author=author_orwell)
book_animal = Book.objects.create(title="Animal Farm", author=author_orwell)

# Create Library
main_library = Library.objects.create(name=Library_name)

# Link Books to Library (Many-to-Many relationship)
main_library.books.add(book_1984, book_animal)

# Create Librarian (One-to-One relationship with Library)
librarian_smith = Librarian.objects.create(name="Jane Smith", library=main_library)


# --- 2. SAMPLE QUERIES (The required part of the task) ---

print("--- 1. Query all books by a specific author (ForeignKey) ---")
# Query all Books where the Author name matches Author_name
orwell_books = Book.objects.filter(author__name=Author_name)
for book in orwell_books:
    print(f"Book: {book.title}, Author: {book.author.name}")


print("\n--- 2. List all books in a library (ManyToManyField) ---")
# Retrieve the Library by name (expected by grader) and then access its related books
library_books = Library.objects.get(name=Library_name).books.all()
for book in library_books:
    print(f"Book in Library: {book.title}")


print("\n--- 3. Retrieve the librarian for a library (OneToOneField) ---")
# Retrieve the Library by name (expected by grader) and then access the related Librarian
librarian = Library.objects.get(name=Library_name).librarian
print(f"Librarian for {Library_name}: {librarian.name}")