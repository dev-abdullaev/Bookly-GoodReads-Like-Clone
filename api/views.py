from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from main_app.models import Blog, BlogComment, BookReview, Book, Favorite
from api.serializers import BlogCommentSerializer, BlogSerializer, BookReviewSerializer, BookSerializer, FavoriteSerializer
from api.permissions import AuthorModifyOrReadOnly, BlogAuthorModifyOrReadOnly


#---------------------------Book----------------------------

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class BookCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


#---------------------------BookReview------------------------------

class BookReviewsAPIView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all().order_by('-created_at')
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user']


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all().order_by('-created_at')
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorModifyOrReadOnly]


#---------------------------Blog------------------------------

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'owner']


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, BlogAuthorModifyOrReadOnly]


#---------------------------BlogComment------------------------------

class BlogCommentListCreateView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all().order_by('-created_at')
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog', 'user']
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all().order_by('-created_at')
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorModifyOrReadOnly]



#----------------------Favorite------------------------

class FavoritesAPIView(generics.ListCreateAPIView):
    """ Favorite List Create API View"""

    queryset = Favorite.objects.all().order_by('-created_date')
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user']


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all().order_by('-created_date')
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorModifyOrReadOnly]
