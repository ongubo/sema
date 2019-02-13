from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def home(request):
    context = {
        'users': User.objects.count()
    }
    return render(request, 'blog/home.html', context)


def users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'blog/users.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'blog/login.html')


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'message': 'Hello, World!'
        }
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
