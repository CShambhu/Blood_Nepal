from django.urls import path
from .import views
from blog.views import Delete_Blog, Update_Blog

urlpatterns =[
    path("", views.blog, name="blog"),
    path("write_blog", views.write_blog, name="write_blog"),
    path("read_post/<int:id>", views.read_post, name="read_post"),
    path("delete_blog/<int:pk>", Delete_Blog.as_view(), name='delete_blog'),
    path("update_blog/<int:pk>", Update_Blog.as_view(), name='update_blog'),


]