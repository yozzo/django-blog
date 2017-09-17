from django.shortcuts import render
from django.utils import timezone
from .models import Post
# import pdb

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    # pdb.set_trace()
    return render(request, 'blog/post_list.html', {'posts': posts})

