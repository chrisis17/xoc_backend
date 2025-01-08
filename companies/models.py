from django.db import models

class Companies(models.Model):
    companie_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.companie_name