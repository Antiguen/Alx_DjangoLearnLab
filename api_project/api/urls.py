from django.urls import path
from .views import BookList

# The app_name is useful for namespacing URLs
app_name = 'api'

urlpatterns = [
    # This path is correct for the BookList view
    path('books/', BookList.as_view(), name='book-list'),
]