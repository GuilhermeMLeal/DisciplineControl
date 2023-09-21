from rest_framework import serializers
from api_controle_disciplina.models.task_model import TaskEntity

class TaskSerializer(serializers.ModelSerializer):
    class Meta:  
        model = TaskEntity
        fields = '__all__'

