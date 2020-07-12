from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    return render(request, 'blog/index.html', context={"post_list": post_list})


def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/detail.html', context={'post': post})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')