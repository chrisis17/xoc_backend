from django.db import models

from companies.models import Companies
from roles.models import Roles

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Session(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, default='qwerty')
    session_token = models.CharField(max_length=255, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.user