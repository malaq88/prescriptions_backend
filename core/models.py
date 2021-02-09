from django.db import models
from django.core.exceptions import ValidationError
import requests
from requests.adapters import HTTPAdapter


class Prescription(models.Model):

    clinic = models.IntegerField()
    physician = models.IntegerField()
    patient = models.IntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = ("Prescription")
        verbose_name_plural = ("Prescriptions")

    def __str__(self):
        return self.id
    
    def medico(self):
        return self.physician
    
    def paciente(self):
        return self.patient

    def physicians_validate(medico):
        requests.adapters.DEFAULT_RETRIES = 5
        r = requests.get('https://5f71da6964a3720016e60ff8.mockapi.io/v1/physicians/'+str(medico), 
            headers={ 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJzZXJ2aWNlIjoicGh5c2ljaWFucyJ9.Ei58MtFFGBK4uzpxwnzLxG0Ljdd-NQKVcOXIS4UYJtA',
                    'content-type': 'application/json', }, timeout=10,)
        return r.status_code

    def patient_validate(paciente):
        requests.adapters.DEFAULT_RETRIES = 5
        r = requests.get('https://5f71da6964a3720016e60ff8.mockapi.io/v1/patients/'+str(paciente), 
            headers={ 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
                    'content-type': 'application/json', }, timeout=10,)
        
        return r.status_code

    def metric_services(medico, paciente, clinica):
        medicos = requests.get('https://5f71da6964a3720016e60ff8.mockapi.io/v1/physicians/'+str(medico), headers={'content-type': 'application/json',})
        medico_json = medicos.json()

        pacientes = requests.get('https://5f71da6964a3720016e60ff8.mockapi.io/v1/patients/'+str(paciente), headers={'content-type': 'application/json',})
        paciente_json = pacientes.json()

        clicnicas = requests.get('https://5f71da6964a3720016e60ff8.mockapi.io/v1/clinics/'+str(clinica), headers={'content-type': 'application/json',})
        if (clicnicas.status_code == 200):
            clinica_json = clicnicas.json()
            clinica_id = clinica_json['id']
            clinica_name =  clinica_json['name']
        else:
            clinica_id = '1'
            clinica_name =  'Clinica'            

        r = requests.post('https://5f71da6964a3720016e60ff8.mockapi.io/v1/metrics', 
                  headers={ 'Authorization': 'Bearer SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', 'content-type': 'application/json', }, 
                  json={"clinic_id": clinica_id,
                        "clinic_name": clinica_name,

                        "physician_id": medico_json['id'],
                        "physician_name": medico_json['name'],
                        "physician_crm": medico_json['crm'],

                        "patient_id": paciente_json['id'],
                        "patient_name": paciente_json['name'],
                        "patient_email": paciente_json['email'],
                        "patient_phone": paciente_json['phone']},
                        timeout=10,)
        return 



