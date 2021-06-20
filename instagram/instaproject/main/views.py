from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Feed
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    feeds=Feed.objects.all()
    return render(request, 'home.html', {'feeds':feeds})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_Feed=Feed()
    new_Feed.pub_date = timezone.datetime.now()
    new_Feed.text=request.POST['text']
    new_Feed.image=request.FILES['image']
    new_Feed.author=request.user
    new_Feed.save()
    return redirect('home')

def detail(request, id):
    feed= get_object_or_404(Feed, pk=id)
    return render(request, 'detail.html', {'feed':feed})

def delete(request, id):
    feed = get_object_or_404(Feed, pk=id)
    feed.delete()
    return redirect('home')

def edit(request, id):
    feed = get_object_or_404(Feed, pk=id)
    return render(request, 'edit.html', {'exist_feed':feed})

def update(request, id):
    update_feed = get_object_or_404(Feed, pk=id)
    update_feed.text = request.POST['text']
    update_feed.image=request.FILES['image']
    update_feed.save()
    return redirect('home')
    

def profile(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    feeds = author.feeds.all()
    return render(request, 'profile.html', {'author':author, 'feeds':feeds})

