from rest_framework import serializers
from api_controle_disciplina.models.subject_model import SubjectEntity

# Classe para serialização de dados de matéria
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:   
        
        model = SubjectEntity # Modelo que será serializado (disciplina)
        fields = '__all__' # Inclui todos os campos do modelo para serem serializados


