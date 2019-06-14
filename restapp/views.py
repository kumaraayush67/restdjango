from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Song, Album
from django.shortcuts import get_object_or_404
from .serializers import AlbumSerializers, SongSerializers
from rest_framework.decorators import action
# Create your views here.

# @api_view(['GET', 'POST', ])
# def firstview(request):
#     return Response("ok")

@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({'hello':'world'})

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class SongView(viewsets.ViewSet):

    def list(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializers(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        song = get_object_or_404(Song, id=pk)
        serializer = SongSerializers(song)
        return Response(serializer.data)   

    @action(detail=True, methods=['get'])
    def getsong(self, request, pk=None):
        album = get_object_or_404(Album, id=pk) 
        song = Song.objects.filter(album=album)
        serializer = SongSerializers(song, many=True)
        return Response(serializer.data) 
        