from django.db import models


class RelatorioCache(models.Model):
    """Model opcional para cachear relatórios gerados"""
    tipo_relatorio = models.CharField(max_length=50)
    data_geracao = models.DateTimeField(auto_now_add=True)
    dados_json = models.JSONField()
    
    class Meta:
        ordering = ['-data_geracao']
    
    def __str__(self):
        return f"{self.tipo_relatorio} - {self.data_geracao}"