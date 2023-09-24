from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.student_model import StudentEntity
from api_controle_disciplina.serializers.student_serializer import StudentSerializer  
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseBadRequest



class SpecificStudentView(APIView):
    # Função para pegar um usuário e retornar todos os dados dele
    def get(self, request, pk):
        try:
            student = StudentEntity.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except StudentEntity.DoesNotExist:
            raise Http404

    # Função para atualizar os dados de usuário
    def put(self, request, pk):
        try:
            student = StudentEntity.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentEntity.DoesNotExist:
            raise Response('Student not found', status=status.HTTP_404_NOT_FOUND)

    # Função para remover um usuário
    def delete(self, request, pk):
        try:
            student = StudentEntity.objects.get(pk=pk)
            student.delete()
            return Response('Student excluded with success', status=status.HTTP_204_NO_CONTENT)
        except StudentEntity.DoesNotExist:
            return Response('Student not found', status=status.HTTP_404_NOT_FOUND)

        
        