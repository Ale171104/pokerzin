from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Player, Game, PlayerHasGame
from .serializers import PlayerSerializer, GameSerializer, PlayerHasGameSerializer


class PlayerAPIView(APIView):
    
    def get(self, request):
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many = True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = PlayerSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED) 


class GameAPIView(APIView):
    
    def get(sefl, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many = True)
        return Response(serializer.data)    
    
    
    def post(sefl, request):
        serializer = GameSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class PlayerHasGameAPIView(APIView):
    
    def get(self, request):
        playerHasGame = PlayerHasGame.objects.all()
        serializer = PlayerHasGameSerializer(playerHasGame, many = True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = PlayerHasGameSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)    
