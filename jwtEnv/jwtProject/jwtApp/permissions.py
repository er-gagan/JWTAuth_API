from rest_framework.permissions import IsAdminUser

class IsStudentUser(IsAdminUser):
    def has_permission(self, request, view):
        if request.user.is_staff == False and request.user.is_superuser == False:
            return True

# class IsTeacherUser(IsAdminUser):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_superuser)

class IsAdminOrTeacherUser(IsAdminUser):
    def has_permission(self, request, view):
            if request.user.is_staff == True or request.user.is_superuser == True:
                return True
