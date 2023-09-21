
from django.contrib import admin
from django.urls import path,include
from api_controle_disciplina.views.task_view.task_views import TaskView
from api_controle_disciplina.views.task_view.specific_task_view import SpecificTaskView

urlpatterns = [
    path('', TaskView.as_view(), name='tasks'),
    path('<int:pk>/', SpecificTaskView.as_view(), name='task'),
]
