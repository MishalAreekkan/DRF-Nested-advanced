from rest_framework import serializers
from . models import Singer,Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = '__all__'
    
    def __init__(self, instance=None, *args, **kwargs):
        print(args, kwargs)
        super().__init__(instance, *args, **kwargs)
        
        
