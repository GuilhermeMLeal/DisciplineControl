from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_controle_disciplina.models.subject_model import SubjectEntity
from api_controle_disciplina.serializers.subject_serializer import SubjectSerializer  


class SpecificSubjectView(APIView):

    def get(self,request,pk):
        try:
            subject = SubjectEntity.objects.get(pk=pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)
        
        except SubjectEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            subject = SubjectEntity.objects.get(pk=pk)
        except SubjectEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            subject = SubjectEntity.objects.get(pk=pk)
        except SubjectEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
