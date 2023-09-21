from api_controle_disciplina.views.student_view.student_views import StudentView
from api_controle_disciplina.views.student_view.specific_student_view import SpecificStudentView
from django.urls import path,include

#Criei 2 views para fazer a separação entre funções gerais e específicas
urlpatterns = [
    # Path com base em cadastrar usuários(POST USER) e capturar todos os usuários(GET - ALL).
    path('', StudentView.as_view(), name='students'),
    # Path com base na atualização de usuário, capturar informações sobre ele e deletá-lo
    path('<int:pk>/', SpecificStudentView.as_view(), name='student'),
]
