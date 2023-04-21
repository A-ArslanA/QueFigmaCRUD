from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('edit/<int:pk>', views.EditPost.as_view(), name="edit"),
    path('details/<int:pk>', views.PostDetail.as_view(), name='post-details'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='delete')
]
