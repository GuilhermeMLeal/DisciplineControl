from django.db import models
from api_controle_disciplina.models.student_model import StudentEntity
from api_controle_disciplina.models.subject_model import SubjectEntity

class TaskEntity(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=255)
    homework_date = models.DateField()
    concluded = models.BooleanField(default=False)
    task_student = models.ForeignKey(StudentEntity, on_delete=models.CASCADE) 
    task_subject = models.ManyToManyField(SubjectEntity)  