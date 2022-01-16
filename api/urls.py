from django.urls import path

from api import views


urlpatterns = [
    path("books/", views.BookListAPIView.as_view(), name="book-list"),
    path("book-create/", views.BookCreateAPIView.as_view(), name="book-create"),
    path("books/<int:pk>/", views.BookRetrieveUpdateDestroyAPIView.as_view(), name="review-detail"),
    
    path("reviews/", views.BookReviewsAPIView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", views.BookReviewDetailAPIView.as_view(), name="review-detail"),

    path("blogs/", views.BlogListAPIView.as_view(), name="blog_list"),
    path("blog-create/", views.BlogListCreateAPIView.as_view(), name="blog-create"),
    path('blogs/<int:pk>/', views.BlogRetrieveUpdateDestroyAPIView.as_view(), name="blog-detail"),

    path("blogcomments/", views.BlogCommentListCreateView.as_view(), name="blogcomment_list"),
    path("blogcomments/<int:pk>/", views.BlogCommentRetrieveUpdateDestroyAPIView.as_view(), name="blogcomment_detail"),

    path("favorites/", views.FavoritesAPIView.as_view(), name="favorite-list"),
    path("favorites/<int:pk>/", views.FavoriteDetailAPIView.as_view(), name="favorite-detail"),

]