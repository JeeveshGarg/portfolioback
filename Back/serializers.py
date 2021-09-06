from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'color','image','description','web')

class ProjectSerializer(serializers.ModelSerializer):
    tags=CategorySerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'image', 'tags','need','web','github')
      
class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ('id', 'name', 'color')

class WorkSerializer(serializers.ModelSerializer):
    tags=ValueSerializer(many=True)

    class Meta:
        model = Work
        fields = ('id', 'name', 'description', 'image', 'tags','web','timeperiod')       

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'       