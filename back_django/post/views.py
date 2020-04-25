from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def post(self, request, *args, **kwargs):
    return Response({
      "user": request.data
    })


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer