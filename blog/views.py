from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from blog.models import Blog, Category, Tag


def home(request):
    blog_list = Blog.objects.all()
    cat = Category.objects.all()
    return render(request, 'blog/home.html', {'blogs': blog_list, 'cat': cat})


def single_blog_view(request, cat, slug):
    blog = get_object_or_404(Blog, category__slug=cat, slug=slug)
    cat = Category.objects.all()
    return render(request, 'blog/single_blog_view.html', {'blog': blog, 'cat': cat})


def category_list(request, cat):
    # blog_list = Category.objects.get()
    category = get_object_or_404(Category, slug=cat)
    blog_list = category.blogs.all()
    return render(request, 'blog/category_list.html', {'blogs': blog_list, 'cat': category})


def add_tag(request):
    if request.method == 'POST':
        slug = request.POST.get('blogSlug')
        post = Blog.objects.get(slug=slug)
        tag_names = [t.name for t in Tag.objects.all()]
        return JsonResponse({
            'message': 'success',
            'tags': tag_names,
            'blog': {
                'slug': post.slug,
                'title': post.title
            }
        })
    return JsonResponse({'message': 'error'})
