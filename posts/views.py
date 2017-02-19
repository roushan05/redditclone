from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from . import models

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request,'posts/create.html',{'error':'ERROR: You must include a title and a url to create a Post'})

    else:
        return render(request,'posts/create.html')
def home(request):
    posts = models.Post.objects.order_by('-votes')
    return  render(request,'posts/home.html',{'posts':posts})

def upvote(request,pk):
    if request.method == 'POST':
        post = models.Post.objects.get(pk=pk)
        post.votes += 1
        post.save()
        return redirect('home')

def downvote(request,pk):
    if request.method == 'POST':
        post = models.Post.objects.get(pk=pk)
        post.votes -= 1
        post.save()
        return redirect('home')

def author(request,fk):
    posts = models.Post.objects.filter(author__id= fk)
    author = models.User.objects.get(pk = fk)
    return render(request,'posts/author.html',{'posts':posts,'author':author})
