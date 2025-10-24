from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from learn.models import *
from .serializers import *
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class BlogerViewSet(ModelViewSet):
    serializer_class = BlogerSerializer
    queryset = Bloger.objects.all()

class LearnViewSet(ModelViewSet):
    serializer_class = LearnSerializer
    queryset = Learn.objects.all()

class HeadlineViewSet(ModelViewSet):
    serializer_class = HeadlineSerializer
    queryset = Headline.objects.all()

