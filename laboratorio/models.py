from django.db import models

class Laboratorio(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} - {self.cnpj}"
