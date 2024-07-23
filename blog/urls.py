from django.urls import path
from .import views

urlpatterns =[
    path("", views.blog, name="blog"),
    path("write_blog", views.write_blog, name="write_blog"),
    path("read_post/<int:id>", views.read_post, name="read_post"),

]