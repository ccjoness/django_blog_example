from django.contrib import admin
from blog.models import *

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(TagBlog)
