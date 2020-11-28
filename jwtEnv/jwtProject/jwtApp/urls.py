from .views import ApiRoot, StudentTeacherList, Student, Teacher
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

urlpatterns = [
    path('',ApiRoot.as_view(), name='root'),
    path('all/',StudentTeacherList.as_view(), name='all'),
    path('student/',Student.as_view(), name="student"),
    path('teacher/',Teacher.as_view(), name="teacher"),
    # path('<int:pk>/',pizza_Detail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)