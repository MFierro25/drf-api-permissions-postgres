from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class List(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title