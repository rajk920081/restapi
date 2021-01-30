
from rest_framework import serializers
from blog.models import Category,Post

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =['id','name','datetime']

class PostSerilizer(serializers.ModelSerializer):
    category =CategorySerilizer(many=False)

    class Meta:
        model =Post
        fields = ['id','image','category','title','body','owner']