from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'email', 'type_of_request', 'details', 'attachment']
