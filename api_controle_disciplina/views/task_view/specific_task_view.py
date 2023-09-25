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
        # Tente pegar a tarefa através do seu id, serialize e retorne com seus dados.
        try:
            task = TaskEntity.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return JsonResponse(serializer.data)
        # Não existindo uma tarefa, retorne um 404(NOT FOUND)
        except TaskEntity.DoesNotExist:
            return Http404('Task does not exist, try another',serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    #Função para atualizar os dados de uma tarefa 
    def put(self, request, pk):
        # Tente aplicar um método GET, serialize e se conseguir retorne os dados serializados.
        try:
            subject = TaskEntity.objects.get(pk=pk)
            serializer = TaskSerializer(subject, data=request.data)
            # "Capture" os dados digitados pelo usuário
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # Se não conseguir serializar, foi erro cometido pelo lado do cliente, ou poderia ser até mesmo um erro 500 do próprio servidor.
            return Response('Task serializer error',serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Tarefa inexistente e retorne um não encontrado.
        except TaskEntity.DoesNotExist:
            raise Response('Task not found', status=status.HTTP_404_NOT_FOUND)
    
    #Aqui está a remoção de uma tarefa.
    def delete(self, request, pk):
        # Tente deletar uma tarefa e se conseguir retorne uma disciplina excluida com sucesso.
        try:
            subject = TaskEntity.objects.get(pk=pk)
            # Delete uma tarefa e retorne um 204.
            subject.delete()
            return Response('Task excluded with success', status=status.HTTP_204_NO_CONTENT)
        # Se não conseguir, significa que a tarefa não existe e retorne um 404.
        except TaskEntity.DoesNotExist:
            return Http404('Task not found', status=status.HTTP_404_NOT_FOUND)   
    