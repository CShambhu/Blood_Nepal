from django.urls import path
from blood_banks import views
urlpatterns = [
    path('', views.banks, name='banks' ),
]
