from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    postlistview,
    postdetailview,
    blogcreateview,
    blogupdateview,
    blogdeleteview,
)

urlpatterns = [
    path('post/<int:pk>/delete/', blogdeleteview.as_view(), name ='post_delete'),
    path('post/<int:pk>/edit/', blogupdateview.as_view(), name='post_edit'),
    path('post/new/', blogcreateview.as_view(), name='post_new'),
    path('', postlistview.as_view(), name='home'),
    path('post/<int:pk>/', postdetailview.as_view(), name='post_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]