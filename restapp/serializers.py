from rest_framework import serializers
from .models import Album, Song

class AlbumSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = ('__all__')

class SongSerializers(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('__all__')