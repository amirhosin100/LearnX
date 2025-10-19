from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.views import APIView
from .serializers import *
from rest_framework import permissions
from rest_framework.response import Response
from user.models import User
from rest_framework.decorators import action
from rest_framework import status,generics
from rest_framework import authentication

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(detail=False,methods=["POST"])
    def get_is_staff(self,request):
        users = self.queryset.filter(is_staff=True)
        serializer = self.get_serializer(users,many=True,context={"request":request})
        return Response(serializer.data)


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=False,methods=["GET"],url_path="status")
    def show_true_status(self,request):
        status = bool(int(request.GET.get("status",1)))

        if status == True or status == False :
            posts = self.queryset.filter(status=status)
            serializer = self.get_serializer(posts,many=True,context={"request":request})
            return Response(serializer.data)
        else:
            return Response({"error":"Error"})

class TicketView(APIView):
    permission_classes = []
    def post(self,request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "تیکت با موفقیت ثبت شد!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset().filter(bloger=request.user.bloger)
        serializer = self.get_serializer(posts,many=True)
        return Response(serializer.data)
