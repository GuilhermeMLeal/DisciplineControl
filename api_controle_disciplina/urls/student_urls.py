from api_controle_disciplina.views.student_view.student_views import StudentView
from api_controle_disciplina.views.student_view.specific_student_view import SpecificStudentView
from django.urls import path,include

#Criei 2 views para fazer a separação entre funções gerais e específicas
urlpatterns = [
    # Path com objetivo de cadastrar usuário(POST USER) e capturar todos os usuários, com as suas devidas informações(GET - ALL).
    path('', StudentView.as_view(), name='students'),
    # Path com funções de atualizar um usuário(PUT), capturar informações sobre ele(GET) e deletá-lo(DELETE).
    path('<int:pk>/', SpecificStudentView.as_view(), name='student'),
    #   
    #path('<int:pk>/task/')
]
