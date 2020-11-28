
from django.contrib.auth.models import User
from .serializers import UserSerializer
# superuser and password = jwt
# from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.db.models import Q


class StudentTeacherList(APIView):
    def get(self, request, format = None):
        stTech = User.objects.exclude(is_staff=True).all()
        stTech_serializer = UserSerializer(stTech, many=True)
        return Response(stTech_serializer.data)

class Student(APIView):
    def get(self, request, format = None):
        st = User.objects.exclude(Q(is_staff=True) | Q(is_superuser=True))
        st_serializer = UserSerializer(st, many=True)
        return Response(st_serializer.data)

class Teacher(APIView):
    def get(self, request, format = None):
        st = User.objects.exclude(Q(is_staff=True) | Q(is_superuser=False))
        st_serializer = UserSerializer(st, many=True)
        return Response(st_serializer.data)

class ApiRoot(APIView):
    def get(self, request, format = None):
        return Response({
            "List Teachers and Student's Record": reverse('all',request=request, format=format),
            "List Student's Data": reverse('student',request=request, format=format),
            "List Teacher's Data": reverse('teacher',request=request, format=format),
        })