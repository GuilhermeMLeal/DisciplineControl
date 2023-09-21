from rest_framework import serializers
from api_controle_disciplina.models.task_model import TaskEntity

# Classe para serialização de dados de tarefas
class TaskSerializer(serializers.ModelSerializer):
    class Meta:  
        #Captando o modelo de tarefas e todos seus campos
        model = TaskEntity
        fields = '__all__'

