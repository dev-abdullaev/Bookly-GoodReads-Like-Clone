from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models import Avg




class Category(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=150)

    class Meta:
        ordering = ["title"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})



class Blog(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='blog/')
    body = models.TextField()
    slug = models.SlugField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)



class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name}"

    # def get_add_to_cart_url(self):
    #     return reverse("add-to-cart", kwargs={"slug": self.slug})

    # def get_remove_from_cart_url(self):
    #     return reverse("remove-from-cart", kwargs={"slug": self.slug})

        

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)





class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.stars_given} stars for {self.book.name} by {self.user.username}"





class Favorite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    created_date = models.DateTimeField(auto_now_add=True)