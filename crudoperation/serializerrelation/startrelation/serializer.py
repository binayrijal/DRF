from rest_framework import serializers
from .models import Singer,Song

class SingerSerializer(serializers.ModelSerializer):
    #songs=serializers.StringRelatedField(many=True,read_only=True)
    #songs=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    songs=serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model=Singer
        fields='__all__'

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model=Song
        fields='__all__'