
from django.contrib import admin
from django.urls import path,include
from api_controle_disciplina.views.subject_view.subject_views import SubjectView
from api_controle_disciplina.views.subject_view.specific_subject_view import SpecificSubjectView

#Criei 2 views para fazer a separação entre funções gerais e específicas.
urlpatterns = [
    # Path com base em cadastrar matérias(POST SUBJECT) e capturar todas as matérias(GET - ALL).
    path('', SubjectView.as_view(), name='subjects'),
    # Path com base na atualização de matérias(PUT), capturar informações sobre ele(GET) e deletá-lo(DELETE)
    path('<int:pk>/', SpecificSubjectView.as_view(), name='subjects'),
]
