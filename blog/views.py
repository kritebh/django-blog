from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import AddPostForm,UpdatePostForm
from .models import Post,Category
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name='blog/homepage.html'
    ordering = ['-post_created_at']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name ='blog/post_detail.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context


class AddPostView(LoginRequiredMixin,CreateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    form_class = AddPostForm
    template_name="blog/add_post.html"
    # fields = '__all__'
    # fields = ('title','body')

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/update_post.html'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/u/login/'
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('homepage')


def post_by_category(request,name):
    # category = Category.objects.get(id=id)
    get_cat_id = Category.objects.filter(name=name).values_list('pk',flat=True)
    post = Post.objects.filter(category_id=int(get_cat_id[0]))
    return render(request,'blog/category_post.html',{'post':post,'category':name})