from rest_framework import serializers
from .models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Prescription
        fields = ['clinic', 'physician', 'patient', 'text']