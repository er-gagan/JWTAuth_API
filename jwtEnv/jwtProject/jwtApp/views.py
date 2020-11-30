
from .models import User
from .serializers import StudentSerializer, TeacherSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from .permissions import IsAdminOrTeacherUser

class StudentTeacherList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, format = None):
        stTech = User.objects.exclude(is_staff=True)
        stTech_serializer = StudentSerializer(stTech, many=True)
        return Response(stTech_serializer.data)       

class Student(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminOrTeacherUser]
    def get(self, request, format = None):
        st = User.objects.filter(Occupation__iexact="Student")
        st_serializer = StudentSerializer(st, many=True)
        return Response(st_serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Student_CRUD(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminOrTeacherUser]
    def get_object(self, pk):
            try:
                return User.objects.get(id=pk)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format = None):
        usr = self.get_object(pk)
        serializer = StudentSerializer(usr)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        usr = self.get_object(pk)
        serializer = StudentSerializer(usr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        usr = self.get_object(pk)
        usr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class studentList(APIView):
    def get(self, request, format = None):
        st = User.objects.filter(Occupation__iexact="Student")
        st_serializer = StudentSerializer(st, many=True)
        return Response(st_serializer.data)

class Teacher(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, format = None):
        tech = User.objects.filter(Occupation__iexact="Teacher")
        tech_serializer = TeacherSerializer(tech, many=True)
        return Response(tech_serializer.data)

    def post(self, request, format = None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Teacher_CRUD(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
            try:
                return User.objects.get(id=pk)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format = None):
        usr = self.get_object(pk)
        serializer = TeacherSerializer(usr)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        usr = self.get_object(pk)
        serializer = TeacherSerializer(usr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        usr = self.get_object(pk)
        usr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiRoot(APIView):
    def get(self, request, format = None):
        return Response({
            "List Teachers and Student's Record": reverse('all',request=request, format=format),
            "Create/Read/Update/Delete Teacher's Records": reverse('Teacher',request=request, format=format),
            "Create/Read/Update/Delete Student's Records": reverse('Student',request=request, format=format),
            "List Student's Records": reverse('studentList',request=request, format=format),
        })

# superuser and password = jwt