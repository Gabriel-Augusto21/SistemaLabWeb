from django.db import models
from dentista.models import Dentista
from cliente.models import Cliente

class Cronograma(models.Model):
    PRIORIDADE_CHOICES = [
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
        ('URGENTE', 'Urgente'),
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE, related_name='cronogramas')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='MEDIA')
    concluido = models.BooleanField(default=False)
    
    observacoes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['data_inicio']
    
    def __str__(self):
        return f"{self.titulo} - {self.dentista.nome}"
