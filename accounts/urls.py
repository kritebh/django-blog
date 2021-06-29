from django.urls import path
from .views import UserRegisterView,UserSettingsView,PasswordsChangeView,password_success,UserInfoEdit,AddInfoView
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('addinfo/',AddInfoView.as_view(),name='add_info'),
    path('edit/',UserSettingsView.as_view(),name='settings'),
    path('<int:pk>/edit_info/',UserInfoEdit.as_view(),name='edit_info'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'),name='change_password'),
    path('password_success',password_success,name='password_success'),
]
