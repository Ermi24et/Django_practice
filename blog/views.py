from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'title 1',
        'content': 'content 1',
        'posted_on': 'January, 2018'
    },
    {
        'author': 'jade mi',
        'title': 'title 2',
        'content': 'content 2',
        'posted_on': 'January, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})