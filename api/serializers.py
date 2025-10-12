from rest_framework import serializers
from learn.models import Learn

class LearnSerializer(serializers.ModelSerializer):
    class Meta :
        model = Learn
        fields = ["id","title","teacher","price","precent_off","discount_price"]