from rest_framework import serializers

from main_app.models import Blog, Book, BookReview, Favorite, BlogComment, Category
from users.models import CustomUser



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title' ]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']



class BookSerializer(serializers.ModelSerializer):
    summary = serializers.CharField()  

    class Meta:
        model = Book
        fields = ('id', 'name', 'category', 'summary','author', 'price', 'discount_price', 'is_active', 'is_new')



class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ['id','user', 'book', 'book_id', 'stars_given', 'comment']



class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)

    

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'user', 'book_id']



class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    summary = serializers.CharField()  

    class Meta:
        model = Blog
        fields = ['id','title', 'summary', 'owner']



class BlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    blog = BlogSerializer(read_only=True)
    blog_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = BlogComment
        fields = ['id', 'user', 'blog', 'blog_id', 'stars_given', 'comments' ]




