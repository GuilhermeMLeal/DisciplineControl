from rest_framework import serializers
from api_controle_disciplina.models.student_model import StudentEntity

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntity
        fields = '__all__'
