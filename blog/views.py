from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Blog, Category


def home(request):
    blog_list = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blog_list})


def single_blog_view(request, cat, slug):
    blog = get_object_or_404(Blog, category__slug=cat, slug=slug)
    return render(request, 'blog/single_blog_view.html', {'blog': blog})


def category_list(request, cat):
    # blog_list = Category.objects.get()
    category = get_object_or_404(Category, slug=cat)
    blog_list = category.blogs.all()
    return render(request, 'blog/category_list.html', {'blogs': blog_list, 'cat': category})
