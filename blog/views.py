from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Blog
from .serializers import CategorySerializer


# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogView(ModelViewSet):
    queryset = Blog.objects.filter.all()
    serializer_class = None
