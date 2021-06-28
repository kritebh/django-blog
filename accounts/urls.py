from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordsChangeView,password_success
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit/',UserEditView.as_view(),name='edit'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'),name='change_password'),
    path('password_success',password_success,name='password_success'),
]
