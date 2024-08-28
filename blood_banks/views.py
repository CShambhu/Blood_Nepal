from django.shortcuts import render
# Create your views here.
def banks(request):
    return render(request,'blood_banks/banks.html')