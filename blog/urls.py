from django.urls import path

from .views import HomeView,PostDetailView,AddPostView,UpdatePostView,PostDeleteView, like_post,post_by_category,author_page,AddCommentView,search

urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('post/<int:pk>',PostDetailView.as_view(),name='detail'),
    path('addpost/',AddPostView.as_view(),name='addpost'),
    path('edit/<int:pk>/',UpdatePostView.as_view(),name='edit'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='delete'),
    path('category/<str:name>/',post_by_category,name='category'),
    path('author/<str:author>/',author_page,name='author_page'),
    path('like/<int:pk>',like_post,name="like"),
    path('search/',search,name="search"),
    path('post/<int:pk>/addcomment/',AddCommentView.as_view(),name='add_comment'),
]
