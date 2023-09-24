
from django.contrib import admin
from django.urls import path,include
from api_controle_disciplina.views.task_view.task_views import TaskView
from api_controle_disciplina.views.task_view.specific_task_view import SpecificTaskView

#Criei 2 views para fazer a separação entre funções gerais e específicas
urlpatterns = [
    # Path com objetivo em cadastrar tarefa(POST TASK) e capturar todas as tarefas, com as suas devidas informações (GET - ALL).
    path('', TaskView.as_view(), name='tasks'),
    # Path com base na atualização de tarefa(PUT), capturar informações sobre ela(GET) e deletá-la(DELETE).
    path('<int:pk>/', SpecificTaskView.as_view(), name='task'),
]
