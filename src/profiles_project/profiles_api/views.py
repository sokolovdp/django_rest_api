from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers, models, permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.NameSerializer

    def list(self, request):
        viewset = [
            'Used methods: list, create, retrieve, update, partial_update, destroy',
            'Automaticaly maps to URLs using Routers',
            'Provides more functionality with less code'
            ]
        return Response({'message': 'Viewset', 'a_viewset': viewset })

    def create(self, request):
        serializer = serializers.NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = '{} you too fuck off !!!'.format(name)
            return Response({'message': message}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        return Response({'message': 'retrive or GET', 'pk': pk})

    def update(self, request, pk=None):
        return Response({'message': 'update or PUT', 'pk': pk})

    def partial_update(self, request, pk=None):
        return Response({'message': 'update or PATCH', 'pk': pk})

    def destroy(self, request, pk=None):
        return Response({'message': 'destroy or DELETE', 'pk': pk})


class HelloApiView(APIView):

    serializer_class = serializers.NameSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Used methods: get, post, put, patch, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.NameSerializer(data=request.data)
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
