from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import date
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.forms import BlogForm
from profile_.models import SignUp
from django.views.generic.edit import DeleteView, UpdateView


# Create your views here.
def read_post(request,id):
    username = request.user.username # Gets the username of user who is logged in from User table
    blog = Blog.objects.get(id=id)
    blog_post = Blog.objects.all()
    #signup = SignUp.objects.get (user = request.user) #Gets the SignUp data of loggedin user
    return render(request, "blog/read_post.html",{'blog':blog, 'username': username,'blog_post':blog_post})

@login_required
def write_blog(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    # signup_user = Blog.objects.all()
    # signup = SignUp.objects.get (user = request.user) #Gets the SignUp data of loggedin user
    signup_user = SignUp.objects.all()
    blog_form = BlogForm()
    context = {'username':username, 'blog_form':blog_form,'signup_user':signup_user} 
    user_profile = SignUp.objects.filter(user=request.user).exists()
    if user_profile:
        if request.method == "POST":
            user = request.user
            signup = SignUp.objects.get(user=request.user)
        blog_form = BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            title = blog_form.cleaned_data['title']
            date = blog_form.cleaned_data['date']
            content = blog_form.cleaned_data['content']
            am = Blog.objects.create(
                user = user,
                signup = signup,
                title = title,
                date = timezone.now(),
                content = content
                )
            am.save()
            messages.success(request,('You have created a blog post.'))
            return redirect('blog')
            
        else:
            blog_form = BlogForm()
    else:
        messages.success(request,('Please complete your profile to write blog.'))
        return redirect('blog')
    return render(request, "blog/write_blog.html", context)



def blog(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    blog_post = Blog.objects.all()
    context = {'username':username,'blog_post':blog_post}
    return render(request, "profile/home.html", context)


class Delete_Blog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context

class Update_Blog(Delete_Blog, UpdateView):
    template_name = "blog/update_blog.html"
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context