from django.db import models



class Base(models.Model):
    creation = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    
    class Meta:
        abstract = True



class Game(Base):
    name = models.TextField(max_length = 100, blank = True)
    number_players = models.IntegerField()
    round_limit = models.IntegerField()
    start_chips_minimum = models.IntegerField()
    start_chips_maximum = models.IntegerField()
    
    class Meta:
        verbose_name = 'Game'
        
        def __str__(self):
            return self.name
        


class Player(Base):
    game = models.ManyToManyField(
        Game,
        through = 'PlayerHasGame',
        through_fields = ("player", "game"))
          
    nickname = models.CharField(max_length = 60, unique = True)
    poker_chips = models.IntegerField()
    points = models.DecimalField(max_digits = 7, decimal_places = 2)
    
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players' 
        
        def __str__(self):
            return self.nickname
    


class PlayerHasGame(Base):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    player_game_chips = models.IntegerField()
    player_in_game = models.BooleanField(default = True)
    player_position = models.IntegerField()
    
    class Meta:
        
        def __str__(self):
            return f"{self.player.nickname} has joined {self.game.name}"
    
    
         