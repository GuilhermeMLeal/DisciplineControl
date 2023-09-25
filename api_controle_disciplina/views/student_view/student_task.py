from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from api_controle_disciplina.models import TaskEntity, StudentEntity
from api_controle_disciplina.serializers.task_serializer import TaskSerializer
from api_controle_disciplina.serializers.student_serializer import StudentSerializer

class TaskStudentView(APIView):
    def get(self, request, pk):
        # Verifique se o aluno existe, caso contrário, retorne um erro 404
        try:
            student = StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            return Http404('Student not found', status=status.HTTP_404_NOT_FOUND)

        # Recupere todas as tarefas relacionadas ao aluno
        tasks = TaskEntity.objects.filter(task_student=student)

        # Serializar as informações do aluno
        serializer_student = StudentSerializer(student)

        # Serializar as tarefas
        serializer = TaskSerializer(tasks, many=True)

        # Crie um dicionário que inclui as informações do aluno e a lista de tarefas, para efetuar o retorno completo.
        response_data = {
            'aluno': serializer_student.data,
            'tarefas': serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)

