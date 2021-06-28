from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# from .forms import UpdatePostForm,AddPostForm
from .models import Post,Category
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name='blog/homepage.html'
    ordering = ['-id']

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
        like_obj = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = like_obj.total_likes()
        context["cat_menu"]=cat_menu
        context["total_likes"] = total_likes
        return context


class AddPostView(LoginRequiredMixin,CreateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    # form_class = AddPostForm
    fields = ('title','featured_image','category','body')
    template_name="blog/add_post.html"
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    fields = ('title','featured_image','category','body')
    template_name = 'blog/update_post.html'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/u/login/'
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('homepage')


def post_by_category(request,name):
    # category = Category.objects.get(id=id)
    get_cat_id = Category.objects.filter(name=name).values_list('pk',flat=True)
    post = Post.objects.filter(category_id=int(get_cat_id[0])).order_by('-post_created_at')
    cat_menu = Category.objects.all()
    return render(request,'blog/category_post.html',{'post':post,'category':name,'cat_menu':cat_menu})

def like_post(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail',args=[str(pk)]))