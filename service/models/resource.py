from django.db import models

from service.models import TrainingModule


class Resource(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='')
    modules = models.ManyToManyField(TrainingModule, related_name='resources')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'resource'
