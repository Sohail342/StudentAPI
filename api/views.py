from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer

class StudentsList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
