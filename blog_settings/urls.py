"""blog_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as b_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', b_views.home, name='home'),
    path('b/create/', b_views.create_blog, name='create_blog'),
    path('b/<slug:cat>/<slug:slug>/', b_views.single_blog_view, name='single_blog_view'),
    path('b/<slug:cat>/', b_views.category_list, name='category_list'),

    # API URL's
    path('api/add_tag/', b_views.add_tag, name='add-tag'),

    # Authentication URL's
    path('register/', b_views.register, name='register'),
    path('login/', b_views.log_in_view, name='login'),
    path('logout/', b_views.log_out, name='logout'),
]
