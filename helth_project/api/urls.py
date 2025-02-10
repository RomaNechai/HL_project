from django.urls import path

from .views import PostViewSet


app_name = 'api'

urlpatterns = [
    path('v1/posts/', PostViewSet.as_view({'get': 'list'})),
    path('v1/posts/<int:pk>/', PostViewSet.as_view({'put': 'update'})),
    path('v1/posts/create/', PostViewSet.as_view({'post': 'create'})),
]