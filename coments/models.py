from django.db import models

from companies.models import Companies

class Coments(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'feedback from {self.customer_name} from {self.company.companie_name}'