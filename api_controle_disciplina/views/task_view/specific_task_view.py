from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.task_model import TaskEntity
from api_controle_disciplina.serializers.task_serializer import TaskSerializer  
from django.http import Http404, JsonResponse

# View específica para uma tarefa
class SpecificTaskView(APIView):
     # Função para pegar uma tarefas e retorne os dados dela
    def get(self,request,pk):
        try:
             # Tente "capturar" uma tarefa através da sua primary key(chave primária) e serialize ele.
            task = TaskEntity.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return JsonResponse(serializer.data)
        # Se não existir/ não encontrar , retorne um 404
        except TaskEntity.DoesNotExist:
            return Http404(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    #Função para atualizar os dados de uma tarefa 
    def put(self, request, pk):
        try:
            # Execute as mesmas funções do método GET (acima)
            subject = TaskEntity.objects.get(pk=pk)
            serializer = TaskSerializer(subject, data=request.data)
            # "Capture" os dados digitados pelo usuário
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskEntity.DoesNotExist:
            raise Response('Task not found', status=status.HTTP_404_NOT_FOUND)
    
    #Aqui está a remoção de um usuário.
    def delete(self, request, pk):
        # Execute um GET e se der certo: 
        try:
            subject = TaskEntity.objects.get(pk=pk)
            # Delete uma tarefa e retorne um 204.
            subject.delete()
            return Response('Task excluded with success', status=status.HTTP_204_NO_CONTENT)
        except TaskEntity.DoesNotExist:
            return Http404('Task not found', status=status.HTTP_404_NOT_FOUND)   
    