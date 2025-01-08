from django.db import models

from users.models import Users

class Chatbots(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Interaction by {self.user.username} at {self.created_at}'
    