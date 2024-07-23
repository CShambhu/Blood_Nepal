from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.utils import timezone
from datetime import date
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.forms import BlogForm
from profile_.models import SignUp


# Create your views here.
def read_post(request,id):
    username = request.user.username # Gets the username of user who is logged in from User table
    blog = Blog.objects.get(id=id)
    blog_post = Blog.objects.all()
    # signup = SignUp.objects.get (user = request.user) #Gets the SignUp data of loggedin user
    return render(request, "blog/read_post.html",{'blog':blog, 'username': username,'blog_post':blog_post})

@login_required
def write_blog(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    # signup_user = Blog.objects.all()
    # signup = SignUp.objects.get (user = request.user) #Gets the SignUp data of loggedin user
    blog_form = BlogForm()
    context = {'username':username, 'blog_form':blog_form}
    if request.method == "POST":
        user = request.user
        signup, created = SignUp.objects.get_or_create(user=user, defaults={'full_name': user.get_full_name(), 'email': user.email})
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            title = blog_form.cleaned_data['title'],
            date = blog_form.cleaned_data['date'],
            content = blog_form.cleaned_data['content'],
            am = Blog.objects.create(
                user = user,
                signup = signup,
                title = title,
                date = timezone.now(),
                content = content
                )
            am.save()
            messages.success(request,('You have created a blog post.'))
            return redirect ( "blog")

    else:
        blog_form = BlogForm()

    return render(request, "blog/write_blog.html", context)

def blog(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    blog_post = Blog.objects.all()
    context = {'username':username,'blog_post':blog_post}
    return render(request, "blog/blog.html", context)
