from django.contrib import admin

from .models import Game, Player, PlayerHasGame

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'number_players',
        'round_limit',
        'start_chips_minimum',
        'start_chips_maximum',
        'creation',
        'update',
        'active'
    )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'poker_chips',
        'points',
        'creation',
        'update',
        'active'
    )


@admin.register(PlayerHasGame)
class PlayerHasGameAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'game',
        'player_game_chips',
        'player_in_game',
        'player_position',
        'creation',
        'update',
        'active'
    )    