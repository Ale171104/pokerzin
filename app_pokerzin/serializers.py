from rest_framework import serializers

from .models import Game, Player, PlayerHasGame

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'number_players',
            'round_limit',
            'start_chips_minimum',
            'start_chips_maximum',
            'creation',
            'update',
            'active'
        )


class PlayerHasGameSerializer(serializers.ModelSerializer):
      
    
    
    class Meta:
        model = PlayerHasGame
        fields = (
            'id',
            'player',
            'game',
            'player_game_chips',
            'player_in_game',
            'player_position',
            'creation',
            'update',
            'active'
        )        

        

class PlayerSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Player
        fields = (
            'id',
            'join_game',
            'nickname',
            'poker_chips',
            'points',
            'creation',
            'update',
            'active'
        )

    def create(self, validated_data):
        join_game_data = validated_data.pop('join_game', None)
        player_instance = Player.objects.create(**validated_data)
        
       
        
            
        return player_instance
            
            
