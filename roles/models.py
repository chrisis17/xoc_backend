from django.db import models

class Roles(models.Model):
    role_name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.role_name