from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("books/", views.BooksView.as_view(), name="list"),
    path("detail/<str:slug>/", views.BookDetailView.as_view(), name="detail"),
    path("reviews/<str:slug>/", views.AddReviewView.as_view(), name="reviews"),
    path("favorite-books/", views.FavoriteBooksView.as_view(), name="favorite_books"),
    path("add-to-favorite/<str:slug>/", views.add_to_favorite, name="add_to_favorite"),
    path('delete_fav_book/<str:slug>/', views.FavBookDeleteView.as_view(), name='delete_fav_book'),
    path('blog-detail/<str:slug>/', views.BlogDetailView, name='blog_detail'),
]
