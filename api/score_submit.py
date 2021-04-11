from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from board.models import User



class ScoreSubmitSerializer(serializers.Serializer):
    score_worth =serializers.IntegerField()
    user_id = serializers.CharField()
    timestamp = serializers.IntegerField()
    
    

