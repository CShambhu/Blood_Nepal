from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from blood_banks.forms import BloodBanksForm
from blood_banks.models import BloodBanks

class BanksView(FormView):
    template_name = 'blood_banks/banks.html'
    form_class = BloodBanksForm
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['username'] = self.request.user.username
        return context