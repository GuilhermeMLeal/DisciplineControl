from django.db import models

class SubjectEntity(models.Model):
    # Modelo de Disciplinas / matérias com campos de nome e descrição.

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    
   # Com modelo de retorno ToString com os 2 parâmetros(nome e descrição)
    def __str__(self) -> str:
        return self.name, self.description
    
    