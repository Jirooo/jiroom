from django.shortcuts import render

from django.views.generic import ListView
from jiroom.models import Post

# Create your views here.
class PostList(ListView):
    model = Post

def top_page(request):
    template_name = 'top_page.html'
    return render(request, template_name)