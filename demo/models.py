from django.db import models

# Create your models here.
class Text(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField() 
    summary = models.TextField(null=True)