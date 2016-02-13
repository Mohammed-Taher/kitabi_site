from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from .models import *

def index(request):
    books_list = book.objects.order_by('title')
    return render(request, 'kitabi/index.html', {'books_list':books_list})

def view_book (request, book_id):
    s_book = get_object_or_404(book, pk=book_id)
    return render(request, 'kitabi/book.html', {'s_book': s_book})

def view_author(request, author_id):
    s_author = get_object_or_404(authors, pk=author_id)
    return render(request, 'kitabi/author.html', {'s_author': s_author})

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")
