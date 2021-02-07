from django.core import exceptions
from django.shortcuts import render
from rest_framework import viewsets
from .models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework.response import Response
from rest_framework import status

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def create(self, request):

        assets = []
        farming_details = {}
        #Set your serializer
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            physicians_status = Prescription.physicians_validate(request.data['physician'])
            patient_status = Prescription.patient_validate(request.data['patient'])

            if (physicians_status == 404):
                return Response({"error": {"message": "physician not found", "code": "02"}}, status=status.HTTP_404_NOT_FOUND)
            elif (patient_status == 404):
                return Response({"error": {"message": "patient not found", "code": "03"}}, status=status.HTTP_400_BAD_REQUEST)
            elif (physicians_status != 200):
                if (physicians_status == 408):
                    return Response({"error": {"message": "physicians service not available", "code": "05"}}, status=status.HTTP_408_REQUEST_TIMEOUT)
                elif (patient_status == 408):
                    return Response({"error": {"message": "patient service not available", "code": "05"}}, status=status.HTTP_408_REQUEST_TIMEOUT)
                else:
                    return Response({"error": {"message": "malformed request", "code": "01"}}, status=status.HTTP_400_BAD_REQUEST)
            else:
                Prescription.metric_services(request.data['physician'],request.data['patient'], request.data['clinic'])
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response(serializer.data, status=status.HTTP_200_OK)

    