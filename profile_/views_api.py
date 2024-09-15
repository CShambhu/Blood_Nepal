from rest_framework import viewsets
from .models import SignUp, Patient
from .serializers import SignUpSerializer, PatientSerializer
from rest_framework.permissions import IsAuthenticated

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    # permission_classes = [IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated]
