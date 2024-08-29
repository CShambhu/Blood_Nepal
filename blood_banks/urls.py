from django.urls import path
from .views import BanksView, BanksDetailView
urlpatterns = [
    path('bank-form/', BanksView.as_view(), name='bank-detail' ),
    path('', BanksDetailView.as_view(), name='detail' ),

]
