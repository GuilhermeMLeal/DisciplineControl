from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.subject_model import SubjectEntity
from api_controle_disciplina.serializers.subject_serializer import SubjectSerializer  

# View geral para matérias
class SubjectView(APIView):
    # Executando um GET e "capturando" todos os dados de matérias existentes e retorne-as.
    def get(self, request):
        disciplina = SubjectEntity.objects.all()
        serializer = SubjectSerializer(disciplina, many=True)
        return Response(serializer.data)
    # Cadastro de matérias
    def post(self, request):
        # Cadastre com base nos dados digitados pelo usuário.
        serializer = SubjectSerializer(data=request.data)
        # Validação se aqueles dados são válidos e salve-os no banco.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
