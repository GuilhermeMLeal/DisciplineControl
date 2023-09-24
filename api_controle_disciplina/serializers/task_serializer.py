from rest_framework import serializers
from api_controle_disciplina.models.task_model import TaskEntity

# Classe para serialização de dados de tarefas
class TaskSerializer(serializers.ModelSerializer):
    class Meta:  
        
        model = TaskEntity # Modelo que será serializado (tarefa)
        fields = '__all__' # Inclui todos os campos do modelo para serem serializados

