from django.urls import path
from . import views

urlpatterns = [
    path('book/list/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/detail/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('author/list/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/detail/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete')
]