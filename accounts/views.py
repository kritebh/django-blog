from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm,UserEditProfile,PasswordsChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class UserEditView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    form_class = UserEditProfile
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('homepage')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(LoginRequiredMixin,PasswordChangeView):
    login_url = '/u/login/'
    redirect_field_name = 'redirect_to'
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('password_success')

@login_required(redirect_field_name='redirect_to',login_url='login/')
def password_success(request):
    return render(request,'registration/password_success.html')