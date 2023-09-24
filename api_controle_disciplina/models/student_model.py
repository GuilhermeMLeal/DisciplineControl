from django.db import models


class StudentEntity(models.Model):
    # Modelo de estudantes / alunos com campos de nome e email.

    name  = models.CharField(blank=False, null=False, max_length=255)
    email = models.CharField(blank=False, null=False, max_length=255)

    # Com retorno ToString com os 2 parâmetros(nome e email)
    def __str__(self) -> str:
        return f'{self.name},{self.email}'