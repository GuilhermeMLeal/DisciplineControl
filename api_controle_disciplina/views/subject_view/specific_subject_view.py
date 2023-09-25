from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.subject_model import SubjectEntity
from api_controle_disciplina.serializers.subject_serializer import SubjectSerializer  
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseBadRequest

# View específica para uma disciplina
class SpecificSubjectView(APIView):
    # Função para pegar uma disciplina e retorne os dados dela
    def get(self,request,pk):
        # Tente pegar a disciplina através do seu id, serialize e retorne com seus dados.
        try:
            subject = SubjectEntity.objects.get(pk=pk)
            serializer = SubjectSerializer(subject)
            return JsonResponse(serializer.data)
        # Não existindo uma disciplina, retorne um 404(NOT FOUND)
        except SubjectEntity.DoesNotExist:
            raise Http404(serializer.errors, status= status.HTTP_404_NOT_FOUND)
   
        
    #Função para atualizar os dados de uma disciplina.
    def put(self, request, pk):
        # Tente aplicar um método GET, serialize e se conseguir retorne os dados serializados.
        try:
            subject = SubjectEntity.objects.get(pk=pk)
            serializer = SubjectSerializer(subject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # Se não conseguir serializar, foi erro cometido pelo lado do cliente, ou poderia ser até mesmo um erro 500 do próprio servidor.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Disciplina inexistente e retorne um não encontrado.
        except SubjectEntity.DoesNotExist:
            raise Response('Subject not found', status=status.HTTP_404_NOT_FOUND)
        
    #Aqui está a remoção de uma disciplina.
    def delete(self, request, pk):
        # Tente deletar uma disciplina e se conseguir retorne um disciplina excluida com sucesso.
        try:
            subject = SubjectEntity.objects.get(pk=pk)
            subject.delete()
            return Response('Subject excluded with success', status=status.HTTP_204_NO_CONTENT)
         # Se não conseguir, significa que a disciplina não existe e retorne um 404.
        except SubjectEntity.DoesNotExist:
            return Response('Subject not found', status=status.HTTP_404_NOT_FOUND)   
    
   
