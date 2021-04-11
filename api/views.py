from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import timezone, datetime
import json
from django.utils.crypto import get_random_string

from api.user_create import UserSerializer, UserLeaderboardSerializer, UserProfileSerializer, UserCreateSerializer
from api.score_submit import ScoreSubmitSerializer
from board.models import User

@api_view(['GET'])
def user_api_view(request, user_id):
    if request.method=='GET':
        user = User.objects.filter(user_id=user_id).first()
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

@api_view(['GET'])
def leaderboard_api_view(request):
    if request.method=='GET':
        user = User.objects.all().order_by('rank')
        serializer = UserLeaderboardSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def leaderboard_country_api_view(request, country):
    if request.method=='GET':
        user = User.objects.filter(country=country).order_by('rank')
        serializer = UserLeaderboardSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def user_create_api_view(request):
    if request.method=='POST':
        if isinstance(request.data, list):
            print("çoklu gönderme")
            for item in request.data:
                print(item)
                if "user_id" not in item:
                    dt = datetime.now()
                    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
                    unique_id = get_random_string(length=32) + str(int(timestamp))
                    item["user_id"] = unique_id
                    # print(request.data["user_id"])

                serializer = UserCreateSerializer(data=item)
        
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.filter(user_id=serializer.data["user_id"]).first()
                    user.rank = User.objects.count()
                    user.save()
            print("fordan çıktım")
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        if "user_id" not in request.data:
            dt = datetime.now()
            timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
            unique_id = get_random_string(length=32) + str(int(timestamp))
            request.data["user_id"] = unique_id
            # print(request.data["user_id"])

        serializer = UserCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(user_id=serializer.data["user_id"]).first()
            user.rank = User.objects.count()
            user.save()
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def score_submit_api_view(request):
    if request.method=='POST':
        if "timestamp" not in request.data:
            dt = datetime.now()
            timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
            request.data["timestamp"] = int(timestamp)
        
        serializer = ScoreSubmitSerializer(data=request.data)
        if serializer.is_valid():

            # some JSON:
            x = serializer.data

            # userr = User.objects.all().order_by('-points')
            # b = 1
            # for user in userr:
            #     user.rank = b
            #     user.save()
            #     b +=1
            # print(userr)
            # the result is a Python dictionary:
            user_id = x["user_id"]
            score_worth = x["score_worth"]
            user = User.objects.filter(user_id=user_id).first()
            user.points += score_worth
            user.save()
            users = User.objects.all().order_by('rank')
            flag = 0
            old_rank = user.rank
            for i in users:
                if user.points >= i.points:
                    user.rank = i.rank
                    user.save()
                    break
                flag += 1
            under_users = users[flag:old_rank]
            # print(under_users)
            for i in under_users:
                if old_rank>i.rank:
                    i.rank += 1
                    i.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)