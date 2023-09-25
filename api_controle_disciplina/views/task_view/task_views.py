from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.task_model import TaskEntity
from api_controle_disciplina.serializers.task_serializer import TaskSerializer  
from django.http import HttpResponseNotFound, Http404, HttpResponseBadRequest

# View geral para tarefas
class TaskView(APIView):
    
    # Executando um GET e "capturando" todos as tarefas existentes e retorne-os.
    def get(self, request):
        # Tente em pegar todos os objetos da entidade tarefas(TaskEntity) e retorne o seus dados.
        try:
            task = TaskEntity.objects.all()
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        # Caso ao contrário, retorne um erro 404 falando que não existe aqueles dados.
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
        # Caso contrário, retorne um erro de requisição feito pelo cliente 
        raise HttpResponseBadRequest(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
