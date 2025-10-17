from rest_framework import serializers
from blog.models import Post
from user.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","url","password"]
        extra_kwargs = {
            "password" :{"write_only":True},
        }


    def create(self, validated_data):
        v = validated_data
        user = User(username=v["username"],first_name=v["first_name"],last_name=v["last_name"])
        user.set_password(v["password"])
        user.save()
        return user

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class TicketSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    content = serializers.CharField(max_length=1000)


    def save(self, **kwargs):
        print(self.validated_data)


    def validate_first_name(self,value):
        if value == "amir":
            raise serializers.ValidationError("خطا داریم")

        return value

class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"
