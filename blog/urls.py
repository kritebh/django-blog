from django.urls import path

from .views import HomeView,PostDetailView,AddPostView,UpdatePostView,PostDeleteView

urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('post/<int:pk>',PostDetailView.as_view(),name='detail'),
    path('addpost/',AddPostView.as_view(),name='addpost'),
    path('edit/<int:pk>/',UpdatePostView.as_view(),name='edit'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='delete'),
]
