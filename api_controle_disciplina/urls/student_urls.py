from api_controle_disciplina.views.student_view.student_views import StudentView
from api_controle_disciplina.views.student_view.specific_student_view import SpecificStudentView
from django.urls import path,include


urlpatterns = [
    path('', StudentView.as_view(), name='students'),
    path('<int:pk>/', SpecificStudentView.as_view(), name='student'),
]
