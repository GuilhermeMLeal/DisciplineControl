from rest_framework import serializers
from api_controle_disciplina.models.student_model import StudentEntity

# Classe para serialização de dados de estudante
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = StudentEntity # Modelo que será serializado(estudante)
        fields = '__all__' # Inclui todos os campos do modelo para serem serializados
