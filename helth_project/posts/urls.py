from django.urls import path

from .views import (PostListView,
                    GroupListView,
                    ProfileListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)


app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='index_list'),
    path('group/<slug:slug>/', GroupListView.as_view(), name='group_list'),
    path('profile/<str:username>/', ProfileListView.as_view(), name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
]