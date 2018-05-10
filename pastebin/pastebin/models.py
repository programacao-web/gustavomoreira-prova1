from django.db import models

# Create your models here.

class Paste(models.Model):
    linguagens = (
        ('Python','Python'),
        ('Javascript','Javascript'),
        ('Outros','Outros'),
    )
    titulo = models.CharField(max_length=200)
    linguagem = models.CharField(max_length=11, choices=linguagens)
    conteudo = models.TextField()