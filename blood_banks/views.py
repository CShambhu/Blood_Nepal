from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from blood_banks.forms import BloodBanksForm
from blood_banks.models import BloodBanks
from profile_.models import SignUp
from django.contrib.auth.models import User
class BanksView(CreateView):
    template_name = 'blood_banks/banks.html'
    form_class = BloodBanksForm
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        # Get the logged-in user
        user = self.request.user
        # Retrieve the SignUp instance associated with the logged-in user
        # sign_up = User.objects.get(user=user)
        # Set the 'added_by' field to the SignUp instance
        form.instance.added_by_user = user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['username'] = self.request.user.username
        return context
    
class BanksDetailView(ListView):
    template_name = 'profile/home.html'
    model = BloodBanks
    context_object_name = 'bankdetails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['username'] = self.request.user.username
        return context

    

    