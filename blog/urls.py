from django.urls import path

from .views import HomeView,PostDetail,AddPostView

urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('post/<int:pk>',PostDetail.as_view(),name='detail'),
    path('addpost/',AddPostView.as_view(),name='addpost')
]
