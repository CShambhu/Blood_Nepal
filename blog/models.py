from django.db import models
from django.utils import timezone
from profile_.models import SignUp
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    signup = models.ForeignKey(SignUp, on_delete=models.CASCADE, null= True)
    title = models.CharField('title',max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    content = models.TextField()
    def __str__(self):
        return self.title

    list_display = ('user', 'title', 'author','date')
  