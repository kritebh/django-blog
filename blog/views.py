from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name='blog/homepage.html'


class PostDetail(DetailView):
    model = Post
    template_name ='blog/article.html'

class AddPostView(CreateView):
    model = Post
    template_name="blog/add_post.html"
    fields = '__all__'
    # fields = ('title','body')