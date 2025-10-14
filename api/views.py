from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from user.models import User
from .serializers import *

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer