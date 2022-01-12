from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("books/", views.BooksView.as_view(), name="list"),
    path("detail/<str:slug>/", views.BookDetailView.as_view(), name="detail"),
    path("read-single-book/<str:slug>/", views.BookReadView.as_view(), name="read_book"),
    path("reviews/<str:slug>/", views.AddReviewView.as_view(), name="reviews"),

    path('edit-book-review/<slug:slug>/<int:review_id>/',
        views.EditReviewView.as_view(), name='edit_book_review'),

    path('confirm-delete-book-review/<slug:slug>/<int:review_id>/',
        views.ConfirmDeleteReviewView.as_view(), name='confirm_delete_book_review'),

    path('delete-book-review/<slug:slug>/<int:review_id>/',
        views.ReviewDeleteView, name='delete_book_review'),

    path("favorite-books/", views.FavoriteBooksView.as_view(), name="favorite_books"),
    path("add-to-favorite/<str:slug>/", views.add_to_favorite, name="add_to_favorite"),

    path('confirm-delete-favorite-book/<slug:slug>/<int:favorite_id>/',
        views.ConfirmDeleteFavoriteView.as_view(), name='confirm_delete_fav_book'),

    path('delete-favorite-book/<slug:slug>/<int:favorite_id>/',
        views.FavBookDeleteView, name='delete_fav_book'),

    path('blog-detail/<str:slug>/', views.BlogDetailView, name='blog_detail'),
    path("comments/<str:slug>/", views.AddBlogCommentView.as_view(), name="comments"),

    path('edit-blog-comment/<slug:slug>/<int:comment_id>/',
        views.EditBlogCommentView.as_view(), name='edit_blog_comment'),

    path('confirm-delete-blog-comment/<slug:slug>/<int:comment_id>/',
        views.ConfirmDeleteBlogCommentView.as_view(), name='confirm_delete_blog_comment'),

    path('delete-blog-comment/<slug:slug>/<int:comment_id>/',
        views.BlogCommentDeleteView, name='delete_blog_comment'),
]
