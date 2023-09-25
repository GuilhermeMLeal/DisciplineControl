from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.student_model import StudentEntity
from api_controle_disciplina.serializers.student_serializer import StudentSerializer  
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseBadRequest , HttpResponseNotFound

# View geral para estudantes
class StudentView(APIView):
    # Executando um GET e capture todos os dados de alunos existentes e retorne-os.
    def get(self, request):
        # Tente em pegar todos os objetos da entidade Alunos(StudentEntity) e retorne o seus dados.
        try:
            student = StudentEntity.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        # Caso ao contrário, retorne um erro 404 falando que não existe aqueles dados.
        except StudentEntity.DoesNotExist:
            raise Http404('Student dont exist , try to add',serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    # Cadastro de disciplina
    def post(self, request):
        # Cadastre com base nos dados digitados pelo usuário.
        serializer = StudentSerializer(data=request.data)
        # Validação se aqueles dados são válidos e salve-os no banco.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Caso contrário, retorne um erro de requisição feito pelo cliente 
        raise HttpResponseBadRequest('Error with fields, try again',serializer.errors, status=status.HTTP_400_BAD_REQUEST)

