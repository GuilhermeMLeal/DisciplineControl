from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.subject_model import SubjectEntity
from api_controle_disciplina.serializers.subject_serializer import SubjectSerializer  
from django.http import Http404, HttpResponseBadRequest, JsonResponse

# View geral para disciplinas
class SubjectView(APIView):
    # Executando um GET e "capturando" todos os dados de matérias existentes e retorne-as.
    def get(self, request):
        # Tente em pegar todos os objetos da entidade Disciplina(SubjectEntity) e retorne o seus dados
        try:
            subjects = SubjectEntity.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return Response(serializer.data)
        # Caso ao contrário, retorne um erro 404 falando que não existe aqueles dados
        except SubjectEntity.DoesNotExist:
            raise Http404('Subject do not exist, try to add one',serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    # Cadastro de matérias
    def post(self, request):
        # Cadastre com base nos dados digitados pelo usuário.
        serializer = SubjectSerializer(data=request.data)
        # Validação se aqueles dados são válidos e salve-os no banco.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Caso contrário, retorne um erro de requisição feito pelo cliente 
        raise HttpResponseBadRequest('Error with fields, try again',serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
