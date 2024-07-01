from rest_framework import serializers
from .models import Student
from userinfo.models import *

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = "__all__"
    category = categorySerializer(read_only = True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        return User_info.objects.create(category=Category.objects.get(),**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    user = userSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
   
