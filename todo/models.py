from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    STATUS_CHOICES = (
        ('Done','Done'),
        ('Not Done','Not Done')
    )
    COLOR_CHOICES = (
        ('Success','success'),
        ('Danger','Danger'),
        ('Warning','Warning'),
        ('Info','Info'),
        ('Light','Light'),
    )
    title = models.CharField(max_length=125)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Not Done')
    due_on = models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='Light')
    done_time = models.DateTimeField(blank=True, null=True, default=None)