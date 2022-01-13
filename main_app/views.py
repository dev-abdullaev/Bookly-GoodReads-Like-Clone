from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import View, ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import MultipleObjectsReturned
from main_app.models import Book, Blog, BookReview, Favorite, BlogComment
from main_app.forms import BookReviewForm, BlogCommentForm



# -------------------Book------------------

def index(request):
    books = Book.objects.filter(is_active=True)
    new_books = Book.objects.filter(is_new=True)
    reviews = BookReview.objects.all()
    blogs = Blog.objects.all()



    context = {'books': books,'new_books': new_books, 
               "reviews": reviews,"blogs": blogs }
    return render(request, 'index.html', context)

    
class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('slug')
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(
                Q(name__icontains=search_query) |
                Q(category__title__icontains=search_query) 
                ).distinct()

        page_size = request.GET.get('page_size', 4)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(request,"book/list.html",{"page_obj": page_obj, "search_query": search_query})


class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        

        return render(request, "book/detail.html", {"book": book})


class BookReadView(LoginRequiredMixin, View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        review_form = BookReviewForm()

        return render(request, "book/read_book.html", {"book": book, "review_form": review_form})

# -------------------Book Review----------------

class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, slug):
        book = Book.objects.get(slug=slug)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )

            return redirect(reverse("read_book", kwargs={"slug": book.slug}))

        return render(request, "book/detail.html", {"book": book, "review_form": review_form})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, slug, review_id):
        book = Book.objects.get(slug=slug)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)


        return render(request, "book/review_update.html", {"book": book, "review": review, 'review_form': review_form})

        
    def post(self, request, slug, review_id):
        book = Book.objects.get(slug=slug)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("read_book", kwargs={"slug": book.slug}))

        return render(request, "book/review_update.html", {"book": book, 'review': review, "review_form": review_form})


class ConfirmDeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, slug, review_id):
        book = Book.objects.get(slug=slug)
        review = book.bookreview_set.get(id=review_id)

        return render(request, "book/confirm_delete_review.html", {"book": book, "review": review})


@login_required
def ReviewDeleteView(request, slug, review_id):
    book = Book.objects.get(slug=slug)
    review = book.bookreview_set.get(id=review_id)

    review.delete()
    return redirect(reverse("read_book", kwargs={"slug": book.slug}))


# ----------------------Favorite-----------------------

@login_required
def add_to_favorite(request, slug):
    book = get_object_or_404(Book, slug=slug)  
    favorites, created = Favorite.objects.get_or_create(
        book=book,
        user=request.user,
        slug=slug
    )

    book = favorites
    return redirect("favorite_books")


class FavoriteBooksView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = "favorite/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorites = Favorite.objects.filter(user=self.request.user)
        context["favorites"] = favorites
        return context


class ConfirmDeleteFavoriteView(LoginRequiredMixin, View):
    def get(self, request, slug, favorite_id):
        book = Book.objects.get(slug=slug)
        favorite = book.favorite_set.get(id=favorite_id)

        return render(request, "favorite/confirm_delete.html", {"book": book, "favorite": favorite})


@login_required
def FavBookDeleteView(request, slug, favorite_id):
    book = Book.objects.get(slug=slug)
    favorite = book.favorite_set.get(id=favorite_id)

    favorite.delete()
    return redirect(reverse("favorite_books"))


# -----------------------Blog--------------------------


def BlogDetailView(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = BookReviewForm()

    return render(request, 'blog/detail.html', {'blog': blog, "comment_form": comment_form})


class AddBlogCommentView(LoginRequiredMixin, View):
    def post(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        comment_form = BlogCommentForm(data=request.POST)

        if comment_form.is_valid():
            BlogComment.objects.create(
                blog=blog,
                user=request.user,
                stars_given=comment_form.cleaned_data['stars_given'],
                comments=comment_form.cleaned_data['comments']
            )

            return redirect(reverse("blog_detail", kwargs={"slug": blog.slug}))

        return render(request, "blog/detail.html", {"blog": blog, "comment_form": comment_form})


class EditBlogCommentView(LoginRequiredMixin, View):
    def get(self, request, slug, comment_id):
        blog = Blog.objects.get(slug=slug)
        comment = blog.blogcomment_set.get(id=comment_id)
        comment_form = BlogCommentForm(instance=comment)


        return render(request, "blog/comment_update.html", {"blog": blog, "comment": comment, 'comment_form': comment_form})

        
    def post(self, request, slug, comment_id):
        blog = Blog.objects.get(slug=slug)
        comment = blog.blogcomment_set.get(id=comment_id)
        comment_form = BlogCommentForm(instance=comment, data=request.POST)

        if comment_form.is_valid():
            comment_form.save()
            return redirect(reverse("blog_detail", kwargs={"slug": blog.slug}))

        return render(request, "blog/comment_update.html", {"blog": blog, 'comment': comment, "comment_form": comment_form})


class ConfirmDeleteBlogCommentView(LoginRequiredMixin, View):
    def get(self, request, slug, comment_id):
        blog = Blog.objects.get(slug=slug)
        comment = blog.blogcomment_set.get(id=comment_id)

        return render(request, "blog/confirm_delete_comment.html", {"blog": blog, "comment": comment})


@login_required
def BlogCommentDeleteView(request, slug, comment_id):
    blog = Blog.objects.get(slug=slug)
    comment = blog.blogcomment_set.get(id=comment_id)

    comment.delete()

    return redirect(reverse("blog_detail", kwargs={"slug": blog.slug}))