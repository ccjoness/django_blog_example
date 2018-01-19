from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey('Category', default=1, related_name='blogs', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return '{} by {} - {}'.format(self.title, self.author.username, self.date)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
