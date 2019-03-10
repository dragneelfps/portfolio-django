from django.shortcuts import render, get_object_or_404

from .models import Blog

def all_blogs(request):
    all_blog_posts = Blog.objects
    return render(request, 'blog/all_blogs.html', { 'all_blog_posts': all_blog_posts })

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', { 'blog': detailblog })
