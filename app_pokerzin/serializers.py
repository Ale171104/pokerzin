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
        )