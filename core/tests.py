
from django.core.checks import messages
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Prescription

class PostTestCase(APITestCase):
    
    def test_lis_all_prescriptions(self):
        url = reverse('prescription-list')

        prescription_1 = Prescription.objects.create(clinic=1, physician=1, patient=1, text= "teste de post")
        prescription_2 = Prescription.objects.create(clinic=2, physician=2, patient=2, text= "teste de post 2")
        prescription_3 = Prescription.objects.create(clinic=3, physician=3, patient=3, text= "teste de post 3")

        response = self.client.get(url, {}, format='json')
        
        self.assertEqual(response.json()[0]['clinic'], prescription_1.clinic)
        self.assertEqual(response.json()[1]['clinic'], prescription_2.clinic)
        self.assertEqual(response.json()[2]['clinic'], prescription_3.clinic)

        self.assertEqual(response.json()[0]['physician'], prescription_1.physician)
        self.assertEqual(response.json()[1]['physician'], prescription_2.physician)
        self.assertEqual(response.json()[2]['physician'], prescription_3.physician)

        self.assertEqual(response.json()[0]['patient'], prescription_1.patient)
        self.assertEqual(response.json()[1]['patient'], prescription_2.patient)
        self.assertEqual(response.json()[2]['patient'], prescription_3.patient)

        self.assertEqual(response.json()[0]['text'], prescription_1.text)
        self.assertEqual(response.json()[1]['text'], prescription_2.text)
        self.assertEqual(response.json()[2]['text'], prescription_3.text)
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_insert_prescription(self):
        url = 'http://localhost:8000/prescriptions/'
        response = self.client.post(url, {'clinic': '1', 'physician':'1', 'patient': '1', 'text': "teste de post"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_physician_not_found(self):
        url = 'http://localhost:8000/prescriptions/'
        response = self.client.post(url, {'clinic': '1', 'physician':'999', 'patient': '1', 'text': "teste de post"}, format='json')

        self.assertEqual(response.json()['error']['message'], 'physician not found')
        self.assertEqual(response.json()['error']['code'], '02')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patient_not_found(self):
        url = 'http://localhost:8000/prescriptions/'
        response = self.client.post(url, {'clinic': '1', 'physician':'1', 'patient': '999', 'text': "teste de post"}, format='json')

        self.assertEqual(response.json()['error']['message'], 'patient not found')
        self.assertEqual(response.json()['error']['code'], '03')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)