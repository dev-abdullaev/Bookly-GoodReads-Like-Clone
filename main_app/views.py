from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DeleteView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Book, Blog, BookReview, Category, Favorite
from .forms import BookReviewForm



def index(request):
    books = Book.objects.filter(is_active=True)
    new_books = Book.objects.filter(is_new=True)
    reviews = BookReview.objects.all()
    blogs = Blog.objects.all()



    context = {'books': books,'new_books': new_books, 
               "reviews": reviews,"blogs": blogs }
    return render(request, 'landing.html', context)

    
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

        return render(request,"list.html",{"page_obj": page_obj, "search_query": search_query})


class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        review_form = BookReviewForm()

        return render(request, "detail.html", {"book": book, "review_form": review_form})


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

            return redirect(reverse("detail", kwargs={"slug": book.slug}))

        return render(request, "detail.html", {"book": book, "review_form": review_form})




@login_required
def add_to_favorite(request, slug):
    book = get_object_or_404(Book, slug=slug)  
    favorites = Favorite.objects.create(
        book=book,
        user=request.user,
        slug=slug
    )
    book = favorites
    return redirect("favorite_books")


class FavoriteBooksView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = "favorite.html"
    context_object_name = "favorites"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorites = Favorite.objects.filter(user=self.request.user)
        context["favorites"] = favorites
        return context


class FavBookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Favorite
    template_name = "fav_delete.html"
    success_url = reverse_lazy("favorite_books")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user




def BlogDetailView( request, slug):
    blog = Blog.objects.get(slug=slug)

    return render(request, "blog_detail.html", {"blog": blog})
