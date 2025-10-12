# for apis
from .serializers import *
from learn.models import Learn
from rest_framework import generics

class LearnListAPIView(generics.ListAPIView):
    queryset = Learn.objects.all()
    serializer_class = LearnSerializer

class LearnDetailAPIView(generics.RetrieveAPIView):
    queryset = Learn.objects.all()
    serializer_class = LearnSerializer