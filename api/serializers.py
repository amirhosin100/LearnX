from rest_framework import serializers
from blog.models import Post
from user.models import *
from learn.models import *

# for user app
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ["url","username","first_name","last_name","email","password"]
        model = User
        extra_kwargs = {
            "password":{"write_only":True}
        }
    def create(self, validated_data):
        password = validated_data["password"]
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

class BlogerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bloger
        fields = "__all__"
# END user app

# for learn app

class HeadlineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Headline
        fields = "__all__"


class LearnSerializer(serializers.HyperlinkedModelSerializer):
    headlines = HeadlineSerializer(many=True)
    class Meta :
        model = Learn
        fields = "__all__"
        read_only_fields = ["discount_price","score"]



