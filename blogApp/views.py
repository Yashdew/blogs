from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)
    #return HttpResponse('<h1>Blog Home Page</h1>')

def about(request):
    return render(request,'blog/about.html')
    return HttpResponse('<h1>Blog Home About</h1>')