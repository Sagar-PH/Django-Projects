from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vault(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file=models.FileField(upload_to='media')
    title=models.CharField(max_length=40)

    def __str__(self):
        return self.title