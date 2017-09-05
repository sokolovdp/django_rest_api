from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets

class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        a_viewset = [
            'Used methods: list, create, reetrive, update, partial_update, delete',
            'Automaticaly maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Viewset', 'a_viewset': a_viewset })




# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Used methods: get, post, put, patch, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Fuck off {}'.format(name)
            return Response({'message': message}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        return Response({'message': 'put'})

    def patch(self, request, pk=None):
        return Response({'message': 'patch'})

    def delete(self, request, pk=None):
        return Response({'message': 'delete'})
