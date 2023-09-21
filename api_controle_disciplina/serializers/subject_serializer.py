from rest_framework import serializers
from api_controle_disciplina.models.subject_model import SubjectEntity

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:   
        model = SubjectEntity
        fields = '__all__'


