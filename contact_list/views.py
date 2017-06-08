#from django.http import HttpResponse
from django.shortcuts import render

from contact_list.models import Blog_post


def index(request):

    posts = Blog_post.objects.all()

    context={
        'postd':posts
    }

    return render(request,'index.html',context)

