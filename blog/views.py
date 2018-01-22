from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from blog.models import Blog, Category, Tag
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        tags_exclude = Tag.objects.all().exclude(blogs__slug=post.slug)
        modal_html = render_to_string('blog/_add_tag_modal.html', {'blog': post, 'other_tags': tags_exclude})
        return JsonResponse({
            'message': 'success',
            'modal_html': modal_html
        })
    return JsonResponse({'message': 'error'})


def register(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password'))
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'blog/register.html', {})


def log_in_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return HttpResponse('That is not a valid user name or password.')
    return render(request, 'blog/login.html', {})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def create_blog(request):
    if request.method == 'POST':

        tags = request.POST.getlist('tags')
        cat = Category.objects.get(slug=request.POST.get('category'))
        blog = Blog()
        blog.title = request.POST.get('title')
        blog.author = request.user
        blog.category = cat
        blog.content = request.POST.get('content')

        blog.save()

        for t in tags:
            tmp_tag = Tag.objects.get(slug=t)
            blog.tag.add(tmp_tag)
        blog.save()
        return HttpResponseRedirect('/')

    return render(request, 'blog/submit_blog.html', {
        'tag': Tag.objects.all(),
        'cat': Category.objects.all()
    })
