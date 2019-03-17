from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=200, default="Unkown Author")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    added_at = models.DateField(auto_now_add=True)
    url = models.URLField()
    author = models.ManyToManyField(Author)
    description = models.TextField()
    slug = models.SlugField()
    cover = models.ImageField(null=True, blank=True, upload_to='uploads/images/')
    categories = models.ManyToManyField(to=Category, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_at']

    def set_slug(self):
        base_slug = slugify(self.title)
        i = 0
        while Book.objects.filter(slug=base_slug).count():
            i += 1
            base_slug += f"-{str(i)}"
        self.slug = base_slug

        self.save()

class Comment(models.Model):
    ratings = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, default='Anonymous', on_delete=models.SET_DEFAULT)
    posted_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(choices=ratings, null=True, blank=True)

    def get_rating(self):
        if self.rating:
            return f"{'⭐' * self.rating}{'- ' * (5-self.rating)}"
        return None
