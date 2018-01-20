from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    super_slug = models.SlugField(blank=True, null=True, unique=True)
    category = models.ForeignKey('Category', default=1, related_name='blogs', on_delete=models.SET_DEFAULT)
    tag = models.ManyToManyField('Tag', related_name='blogs', blank=True)

    def __str__(self):
        return '{} by {} - {}'.format(self.title, self.author.username, self.date)

    def save(self, *args, **kwargs):
        if not self.slug:
            number = 0
            slug_title = slugify(self.title)
            checking = True
            while checking:
                results = Blog.objects.filter(slug=slug_title)
                if results.exists():
                    slug_title = slugify(self.title) + '_' + str(number + 1)
                    number += 1
                else:
                    checking = False
            self.slug = slug_title
        super().save(args, kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            number = 0
            slug_title = slugify(self.name)
            checking = True
            while checking:
                results = Category.objects.filter(slug=slug_title)
                if results.exists():
                    slug_title = slugify(self.name) + '_' + str(number + 1)
                    number += 1
                else:
                    checking = False
            self.slug = slug_title
        super().save(args, kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            number = 0
            slug_title = slugify(self.name)
            checking = True
            while checking:
                results = Tag.objects.filter(slug=slug_title)
                if results.exists():
                    slug_title = slugify(self.name) + '_' + str(number + 1)
                    number += 1
                else:
                    checking = False
            self.slug = slug_title
        super().save(args, kwargs)
