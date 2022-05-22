from django.views.generic import ListView, DetailView
from django.shortcuts import render

from blog.models import Post

# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Create your views here.

def top(request):
    template_name = "top.html"
    return render(request, template_name)

class PostList(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    template_name = "article.html"
    context_object_name = "post"