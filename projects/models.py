from django.db import models

# modelo para emparejar los campos con los de la base de datos

class Project(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
