from django import forms
from blog.models import Blog, Tag


class BlogForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tag']



# from blog.old_forms import BlogForm
#
# @login_required
# def create_blog2(request):
#     form = BlogForm()
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             for t in request.POST.getlist('tag'):
#                 tmp_tag = Tag.objects.get(pk=t)
#                 blog.tag.add(tmp_tag)
#             blog.save()
#             return HttpResponseRedirect('/')
#         return HttpResponse('Error, form not valid.')
#
#     return render(request, 'blog/submit_blogModelForm.html', {
#         'form':form,
#         'tag': Tag.objects.all(),
#         'cat': Category.objects.all()
#     })
