from django.urls import path
from .views import BanksView
urlpatterns = [
    path('', BanksView.as_view(), name='bank-detail' ),

]
