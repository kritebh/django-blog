from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import AddPostForm,UpdatePostForm
from .models import Post
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name='blog/homepage.html'
    ordering = ['-post_created_at']


class PostDetailView(DetailView):
    model = Post
    template_name ='blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name="blog/add_post.html"
    # fields = '__all__'
    # fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/update_post.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('homepage')