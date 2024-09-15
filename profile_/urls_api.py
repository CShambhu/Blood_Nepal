from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import SignUpViewSet, PatientViewSet

router = DefaultRouter()
router.register(r'signup', SignUpViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
