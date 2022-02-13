from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ClientSerializer, PosterSerializer
from .models import Client, Poster
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import base64
#from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
class ClientView(generics.GenericAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientViewDetail(generics.GenericAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def put(self, request, curl):
        # print(curl)
        dcurl = base64.b64decode(curl.encode('utf8')).decode('utf8')
        item = Client.objects.get(curl=dcurl)
        serializer = self.serializer_class(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('OK, update complete.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PosterView(generics.GenericAPIView):

    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

    def post(self, request):
        poster = request.data
        serializer = self.serializer_class(data=poster)

        # Validate client
        reporter = request.data['reporter']
        client = Client.objects.get(curl=reporter)
        if client is None:
            return Response('Error: No such user.', status=status.HTTP_400_BAD_REQUEST)
        
        cli_ip = ''
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            cli_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            cli_ip = request.META.get("REMOTE_ADDR")
        # cli_port = request.META.get("REMOTE_PORT")
        print(client.ipaddr, cli_ip)
        if client.ipaddr != cli_ip:
            return Response('Error: IP addres does not match.', status=status.HTTP_400_BAD_REQUEST)

        # Validate json
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
