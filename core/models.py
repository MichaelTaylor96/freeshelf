from django.db import models

# Create your models here.

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
