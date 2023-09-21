
from django.contrib import admin
from django.urls import path,include
from api_controle_disciplina.views.subject_view.subject_views import SubjectView
from api_controle_disciplina.views.subject_view.specific_subject_view import SpecificSubjectView

urlpatterns = [
    path('', SubjectView.as_view(), name='subjects'),
    path('<int:pk>/', SpecificSubjectView.as_view(), name='subjects'),
]
