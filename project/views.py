from django.shortcuts import render , redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        index = BlogForm(request.POST , request.FILES)
        if index.is_valid():
            index.save()
        return redirect('index')
    context ={
        'pro':BlogForm(),
    }
    return render (request , 'index.html' , context)
def post(request):
    context={
        'postall':Blog.objects.all()
    }
    return render(request , 'post.html' ,context)