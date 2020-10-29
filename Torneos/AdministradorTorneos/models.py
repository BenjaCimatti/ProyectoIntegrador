from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255)


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Player(User):
    country = models.CharField(max_length=255)


class Match(models.Model):
    name = models.CharField(max_length=255)
    match_map = models.CharField(max_length=255)
    match_players = models.ManyToManyField(Player)
    winner = models.ForeignKey(Player, related_name='match_winner', on_delete=models.CASCADE)
    loser = models.ForeignKey(Player, related_name='match_loser', on_delete=models.CASCADE)
    winning_score = models.PositiveIntegerField()
    losing_score = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)