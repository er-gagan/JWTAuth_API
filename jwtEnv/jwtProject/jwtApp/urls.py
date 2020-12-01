from .views import ApiRoot, StudentTeacherList, studentList, Student, Teacher, Student_CRUD, Teacher_CRUD
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verifytoken/',TokenVerifyView.as_view(), name='token_verify'),
    path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    path('',ApiRoot.as_view(), name='root'),
    path('all/',StudentTeacherList.as_view(), name='all'),
    path('teacher/',Teacher.as_view(), name="Teacher"),
    path('teacher/<int:pk>/',Teacher_CRUD.as_view()),
    path('student/',Student.as_view(), name="Student"),
    path('student/<int:pk>/',Student_CRUD.as_view()),
    path('studentList/',studentList.as_view(), name="studentList"),
]
urlpatterns = format_suffix_patterns(urlpatterns) 