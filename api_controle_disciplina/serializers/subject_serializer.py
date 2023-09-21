from rest_framework import serializers
from api_controle_disciplina.models.subject_model import SubjectEntity

# Classe para serialização de dados de matéria
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:   
        #Captando o modelo matéria e todos seus campos
        model = SubjectEntity
        fields = '__all__'


