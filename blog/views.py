from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def index(request):
    post_list = post.objects.order_by('-pub_date')
    categories = category.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list, 'categories': categories})

def show_post(request, post_id):
    s_post = get_object_or_404(post, pk=post_id)
    categories = category.objects.all()
    return render(request, 'blog/post.html', {'s_post': s_post, 'categories': categories})
