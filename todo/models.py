from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    STATUS_CHOICES = (
        ('dn','Done'),
        ('nt','Not Done')
    )
    title = models.CharField(max_length=125)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='nt')
    done_time = models.DateTimeField(blank=True, null=True, default=None)