from django.db import models


class Saida(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.tipo} - R$ {self.valor} ({self.data})"