from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100, 
        help_text="Nome da categoria",
        unique=True,
    )
    description = models.TextField(
        null = True,
        blank=True,
    )



