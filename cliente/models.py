from django.db import models

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome}"
