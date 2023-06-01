from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,


    Responses,
    Respond,
    response_accept,
    response_delete
)

urlpatterns = [
    path('', PostListView.as_view(), name='announcement-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    path('responses', Responses.as_view(), name='responses'),
    path('respond/<int:pk>', Respond.as_view(), name='respond'),
    path('response/accept/<int:pk>', response_accept),
    path('response/delete/<int:pk>', response_delete),
]


