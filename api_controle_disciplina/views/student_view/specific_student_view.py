from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.student_model import StudentEntity
from api_controle_disciplina.serializers.student_serializer import StudentSerializer  
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseBadRequest


class SpecificStudentView(APIView):

    # Função para pegar um aluno e retornar todos os dados dele.
    def get(self, request, pk):
        # Tente pegar o aluno através do seu id, serialize e retorne com seus dados.
        try:
            student = StudentEntity.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)
        # Não existindo o aluno, retorne um 404(NOT FOUND)
        except StudentEntity.DoesNotExist:
            raise Http404(serializer.errors, status = status.HTTP_404_NOT_FOUND)

    # Função para atualizar os dados de um aluno.
    def put(self, request, pk):
        # Tente aplicar um método GET, serialize e se conseguir retorne os dados serializados.
        try:
            student = StudentEntity.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # Se não conseguir serializar, foi erro cometido pelo lado do cliente, ou poderia ser até mesmo um erro 500 do próprio servidor.
            return HttpResponseBadRequest(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Aluno inexistente e retorne um não encontrado.
        except StudentEntity.DoesNotExist:
            raise Http404('Student not found', status=status.HTTP_404_NOT_FOUND)

    # Função para remover um aluno
    def delete(self, request, pk):
        # Tente deletar um aluno e se conseguir retorne um aluno excluido com sucesso.
        try:
            student = StudentEntity.objects.get(pk=pk)
            student.delete()
            return Response('Student excluded with success', status=status.HTTP_204_NO_CONTENT)
        # Se não conseguir, significa que o aluno não existe e retorne um 404.
        except StudentEntity.DoesNotExist:
            return Response('Student not found', status=status.HTTP_404_NOT_FOUND)

        
        