from rest_framework.viewsets import ModelViewSet
from learn.models import *
from .serializers import *
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

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

