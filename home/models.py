from django.db import models
import uuid
from autoslug import AutoSlugField

# Create your models here.

class Convertion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    old_link = models.CharField(max_length=500)
    new_link = models.CharField(max_length=100)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.old_link[0:4]}..."

class ClickLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.ForeignKey(Convertion, on_delete=models.CASCADE, related_name="clicks")
    clicked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.clicked_at}"