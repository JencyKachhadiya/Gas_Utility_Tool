from django.db import models
from django.utils import timezone

class ServiceRequest(models.Model):
    TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Reading', 'Meter Reading'),
        ('Connection Issue', 'Connection Issue'),
    )

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    type_of_request = models.CharField(max_length=100, choices=TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    pending = models.BooleanField(default=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name}'s {self.type_of_request} Request"
    
    def save(self, *args, **kwargs):
        if self.resolved and not self.resolved_at:
            self.resolved_at = timezone.now()
        super().save(*args, **kwargs)
