from django.db import models

# Create your models here.

class livros (models.Model):
    titulo = models.CharField(max_length = 75, null= False, blank= False)
    editora = models.CharField(max_length= 75, null= False, blank= False)
    preco = models.FloatField(null= False, blank= False)

    