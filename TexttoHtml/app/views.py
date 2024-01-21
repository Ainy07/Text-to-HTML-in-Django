from django.shortcuts import render
from .models import Post
from app.forms import PostForm

def home(request):
    form=PostForm()
    return render(request,'home.html',{'form':form})