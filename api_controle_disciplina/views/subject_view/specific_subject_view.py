from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.subject_model import SubjectEntity
from api_controle_disciplina.serializers.subject_serializer import SubjectSerializer  

# View específica para uma matéria
class SpecificSubjectView(APIView):
    # Função para pegar uma matéria e retorne os dados dela
    def get(self,request,pk):
        try:
            # Tente "capturar" uma matéria através da sua primary key(chave primária) e serialize ele.
            subject = SubjectEntity.objects.get(pk=pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)
        # Se não existir/ não encontrar , retorne um 404
        except SubjectEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    #Função para atualizar os dados de uma tarefa 
    def put(self, request, pk):
        # Execute as mesmas funções do método GET (acima)
        try:
            subject = SubjectEntity.objects.get(pk=pk)
        except SubjectEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # "Capture" os dados digitados pelo usuário
        serializer = SubjectSerializer(subject, data=request.data)
        # Se forem válidos:
        if serializer.is_valid():
            #Salve eles e retorne
            serializer.save()
            return Response(serializer.data)
        # Se não, diga que a serialização deu erro e retorne um 404
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Aqui está a remoção de uma matéria.
    def delete(self, request, pk):
        # Execute um GET e se der certo:
        try:
            subject = SubjectEntity.objects.get(pk=pk)
        except SubjectEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete uma tarefa e retorne um 204.
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
