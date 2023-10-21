from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()


def all_blogs(request):
    blogs = Blog.objects.order_by('created_on')
    blog_count = blogs.count
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


def bounties(request):
    blogs = Blog.objects.order_by('created_on')
    return render(request, 'blog/bounties.html', {'blogs': blogs})
