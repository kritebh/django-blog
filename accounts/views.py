from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm,UserSettings,PasswordsChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class UserSettingsView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    form_class = UserSettings
    template_name = 'accounts/settings.html'
    success_url = reverse_lazy('homepage')

    def get_object(self):
        return self.request.user

class AddInfoView(LoginRequiredMixin,generic.CreateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    model = Profile
    template_name = 'accounts/add_info.html'
    fields = ['bio','profile_pic','twitter','instagram','linkedin','facebook','pinterest','github']
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserInfoEdit(LoginRequiredMixin,generic.UpdateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    model = Profile
    template_name = 'accounts/edit_info.html'
    fields = ['bio','profile_pic','twitter','instagram','linkedin','facebook','pinterest','github']
    success_url=reverse_lazy('homepage')

class PasswordsChangeView(LoginRequiredMixin,PasswordChangeView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('password_success')

@login_required(redirect_field_name='redirect_to',login_url='login/')
def password_success(request):
    return render(request,'registration/password_success.html')