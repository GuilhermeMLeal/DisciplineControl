from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.task_model import TaskEntity
from api_controle_disciplina.serializers.task_serializer import TaskSerializer  
from django.http import HttpResponseNotFound, Http404, HttpResponseBadRequest

# View geral para matérias
class TaskView(APIView):
    
    # Executando um GET e "capturando" todos os dados de usuários existentes e retorne-os.
    def get(self, request):
        try:
            task = TaskEntity.objects.all()
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        except TaskEntity.DoesNotExist:
            raise Http404(serializer.error, status = status.HTTP_404_NOT_FOUND)
        
    # Cadastro de tarefas
    def post(self, request):
        # Cadastre com base nos dados digitados pelo usuário.
        serializer = TaskSerializer(data=request.data)
        # Validação se aqueles dados são válidos e salve-os no banco.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise HttpResponseBadRequest(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
