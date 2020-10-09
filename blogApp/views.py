from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author':'Yash Dewangan',
        'title':'blogpost1',
        'content':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'date_posted':'August 27,2020'
    },
    {
        'author':'Sumit kol',
        'title':'blogpost2',
        'content':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'date_posted':'August 28,2020'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request,'blog/home.html',context)
    #return HttpResponse('<h1>Blog Home Page</h1>')

def about(request):
    return render(request,'blog/about.html')
    return HttpResponse('<h1>Blog Home About</h1>')