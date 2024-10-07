from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

# def bloghome(index):
#     return HttpResponse('this is blog home paaage')

# def blogpost(request, slug):
#     return HttpResponse('this is blog post: {slug}') 

def bloghome(request):
    allPosts = Post.objects.all()
    content = {'allPosts': allPosts}
    return render(request, 'blog/bloghome.html', content)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post} 
    return render(request, 'blog/blogpost.html', context)


