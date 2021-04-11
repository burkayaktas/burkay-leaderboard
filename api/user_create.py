from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from board.models import User



class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    display_name = serializers.CharField(max_length=100)
    points = serializers.IntegerField(default=0)
    rank = serializers.IntegerField()
    country = serializers.CharField(default='tr')
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = (
            'display_name', 'points', 'rank', 'country'
        )


class UserLeaderboardSerializer(serializers.Serializer):
    rank = serializers.IntegerField()
    points = serializers.IntegerField(default=0)
    display_name = serializers.CharField(max_length=100)
    country = serializers.CharField(default='tr')

    class Meta:
        model = User
        fields = (
            'display_name', 'points', 'rank', 'country'
        )


class UserProfileSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    display_name = serializers.CharField(max_length=100)
    points = serializers.IntegerField(default=0)
    rank = serializers.IntegerField()
    

    class Meta:
        model = User
        fields = (
            'display_name', 'points', 'rank', 'country'
        )


class UserCreateSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    display_name = serializers.CharField(max_length=100)
    country = serializers.CharField(default='tr')
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = (
            'display_name', 'points', 'rank', 'country'
        )
