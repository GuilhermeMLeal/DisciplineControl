from rest_framework import serializers
from api_controle_disciplina.models.student_model import StudentEntity

# Classe para serialização de dados de estudante
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        #Captando o modelo estudante e todos seus campos
        model = StudentEntity
        fields = '__all__'
