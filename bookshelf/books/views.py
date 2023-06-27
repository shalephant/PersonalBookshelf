from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_edit.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_edit.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_edit.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'books/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')