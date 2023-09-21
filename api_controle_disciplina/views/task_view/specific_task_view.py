from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.task_model import TaskEntity
from api_controle_disciplina.serializers.task_serializer import TaskSerializer  

# View específica para uma tarefa
class SpecificTaskView(APIView):
     # Função para pegar uma tarefas e retorne os dados dela
    def get(self,request,pk):
        try:
             # Tente "capturar" uma tarefa através da sua primary key(chave primária) e serialize ele.
            task = TaskEntity.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        # Se não existir/ não encontrar , retorne um 404
        except TaskEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    #Função para atualizar os dados de uma tarefa 
    def put(self, request, pk):
        try:
            # Execute as mesmas funções do método GET (acima)
            task = TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # "Capture" os dados digitados pelo usuário
        serializer = TaskSerializer(task, data=request.data)
         # Se forem válidos:
        if serializer.is_valid():
            #Salve eles e retorne
            serializer.save()
            return Response(serializer.data)
        # Se não, diga que a serialização deu erro e retorne um 404
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Aqui está a remoção de um usuário.
    def delete(self, request, pk):
        # Execute um GET e se der certo:
        try:
            student = TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete uma tarefa e retorne um 204.
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)