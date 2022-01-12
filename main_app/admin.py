from django.contrib import admin

from main_app.models import Blog, Category, Book, BookReview, Favorite, BlogComment


admin.site.register(Favorite)
admin.site.register(BlogComment)
admin.site.register(BookReview)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Book, BookAdmin)



