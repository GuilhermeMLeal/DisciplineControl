from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.task_model import TaskEntity
from api_controle_disciplina.serializers.task_serializer import TaskSerializer  

# View geral para matérias
class TaskView(APIView):
    
    # Executando um GET e "capturando" todos os dados de usuários existentes e retorne-os.
    def get(self, request):
        task = TaskEntity.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
        
    # Cadastro de tarefas
    def post(self, request):
        # Cadastre com base nos dados digitados pelo usuário.
        serializer = TaskSerializer(data=request.data)
        # Validação se aqueles dados são válidos e salve-os no banco.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
