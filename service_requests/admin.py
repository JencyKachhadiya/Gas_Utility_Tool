from django.contrib import admin
from .models import ServiceRequest
from django.utils import timezone
from django import forms

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'type_of_request', 'pending', 'resolved', 'submitted_at']
    list_filter = ['pending', 'resolved']
    search_fields = ['customer_name', 'type_of_request']
    readonly_fields = ['submitted_at', 'resolved_at']

    def save_model(self, request, obj, form, change):
        if obj.resolved and not obj.resolved_at:
            obj.resolved_at = timezone.now()
        obj.save()

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'resolved':
            kwargs['widget'] = forms.CheckboxInput(attrs={'onclick': 'disablePending()'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(ServiceRequest, ServiceRequestAdmin)