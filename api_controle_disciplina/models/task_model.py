from django.db import models
from api_controle_disciplina.models.student_model import StudentEntity
from api_controle_disciplina.models.subject_model import SubjectEntity

class TaskEntity(models.Model):
    # Modelo de tarefas com campos de titulo, descrição, entrega de tarefa, concluido, relacionamento entre estudante e tarefa e tarefa e matéria.
    title = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=255)
    submit_homework = models.DateField()
    concluded = models.BooleanField(default=False)
    task_student = models.ForeignKey(StudentEntity, on_delete=models.CASCADE) 
    task_subject = models.ManyToManyField(SubjectEntity)  

    # Com retorno ToString com os 3 parâmetros(Titulo, descrição e data de entrega da tarefa)
    def __str__(self) -> str:
        return f'{self.title}, {self.description}, {self.homework_date}'