from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import CategorySerilizer,PostSerilizer
from blog.models import Category,Post
from rest_framework import permissions

class CatViewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerilizer
    permission_classes = [permissions.IsAdminUser]

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]