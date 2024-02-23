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

    
   
class PlayerPutDeleteAPIView(APIView):
    
    def get(self, request, pk):
        try:        
            player = Player.objects.get(pk = pk)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
         
    
    def put(self, request, pk):
        try:        
            player = Player.objects.get(pk = pk)
            
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        serializer = PlayerSerializer(player, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        try:
            player = Player.objects.get(pk = pk)
        except Player.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
            
        player.delete()
        return Response(status = status.HTTP_200_OK)



class GameAPIView(APIView):
    
    def get(sefl, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many = True)
        return Response(serializer.data)    
    
    
    def post(sefl, request):
        serializer = GameSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)



class GamePutDeleteAPIView(APIView):
    
    def get(self, request, pk):
        try:        
            game = Game.objects.get(pk = pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
         
    
    def put(self, request, pk):
        try:        
            game = Game.objects.get(pk = pk)
            
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        serializer = GameSerializer(game, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        try:
            game = Game.objects.get(pk = pk)
        except Game.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
            
        game.delete()
        return Response(status = status.HTTP_200_OK)



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
