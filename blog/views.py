from django.shortcuts import render
from .models import Posts


def Homepage(request):
    '''landing page of dummy site'''

    context = {
        'posts' : Posts.objects.all()
    }

    return render(request, 'blog/home.html', context)

def about(request):
    ''''about of blog application'''
    return render(request, 'blog/about.html', {'title': 'about'})