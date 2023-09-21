from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.student_model import StudentEntity
from api_controle_disciplina.serializers.student_serializer import StudentSerializer  

# View específica para uma estudante
class SpecificStudentView(APIView):
    # Função para pegar um usuário e retornar todo os dados dele
    def get(self,request,pk):
        # Tente "capturar" um usuário através da sua primary key(chave primária) e serialize ele.
        try:
            student = StudentEntity.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        # Se não existir/ não encontrar , retorne um 404
        except StudentEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    #Função para atualizar os dados de usuário    
    def put(self, request, pk):
        # Execute as mesmas funções do método GET (acima)
        try:
            student = StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # "Capture" os dados digitados pelo usuário
        serializer = StudentSerializer(student, data=request.data)
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
            student = StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete um usuário e retorne um 204.
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)