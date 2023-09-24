
from django.contrib import admin
from django.urls import path,include
from api_controle_disciplina.views.subject_view.subject_views import SubjectView
from api_controle_disciplina.views.subject_view.specific_subject_view import SpecificSubjectView

#Criei 2 views para fazer a separação entre funções gerais e específicas.
urlpatterns = [
    # Path com objetivo de cadastrar matéria(POST SUBJECT) e capturar todas as matérias,com as suas devidas informações (GET - ALL).
    path('', SubjectView.as_view(), name='subjects'),
    # Path com funções de atualização de uma matéria (PUT), capturar informações sobre ela(GET) e deletá-la(DELETE).
    path('<int:pk>/', SpecificSubjectView.as_view(), name='subjects'),
]
