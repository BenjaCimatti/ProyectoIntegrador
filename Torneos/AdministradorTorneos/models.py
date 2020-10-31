from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

from django.core.exceptions import ValidationError

class Game(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, editable=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)



class Match(models.Model):
    #name = models.CharField(max_length=25)
    match_map = models.CharField(max_length=30)
    match_players = models.ManyToManyField(Player, blank=True)
    winner = models.ForeignKey(Player, related_name='%(class)s_winner', default='', null=True, blank=True, on_delete=models.CASCADE)
    loser = models.ForeignKey(Player, related_name='%(class)s_loser', default='', null=True, blank=True, on_delete=models.CASCADE)
    winning_score = models.PositiveIntegerField(null=True, blank=True)
    losing_score = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.match_map

class QuarterMatch(Match):
    tournament = models.ForeignKey(Tournament, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

class SemiMatch(Match):
    tournament = models.ForeignKey(Tournament, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return super().__str__()

class FinalMatch(Match):
    final = models.OneToOneField(Tournament, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return super().__str__()