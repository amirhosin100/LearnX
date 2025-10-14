from rest_framework import serializers
from learn.models import Learn
from user.models import Teacher,User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        fields = ["first_name","last_name","username","id"]


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedIdentityField(
        view_name="api:user-detail"
    )
    class Meta:
        model = Teacher
        fields = ["user","address","city"]
        # extra_kwargs = {
        #     'url': {'view_name': 'user', 'lookup_field': 'user'},
        #     'user': {'lookup_field': 'username'}
        # }