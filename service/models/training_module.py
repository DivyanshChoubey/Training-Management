from django.db import models

from service.models import Trainer


class TrainingModule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    created_by = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='modules')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'training_module'
