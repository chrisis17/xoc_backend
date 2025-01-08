from django.db import models

from companies.models import Companies

class Dashboards(models.Model):
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    directory_name = models.CharField(max_length=200)
    
    