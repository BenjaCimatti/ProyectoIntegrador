from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


#class Tournament(models.Model):
 #   name = models.CharField(max_length=255)
  #  game = models.ForeignKey(Game, on_delete=models.CASCADE)
   # def __str__(self):
    #    return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, editable=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)



#class Match(models.Model):
 #   name = models.CharField(max_length=255)
  #  match_map = models.CharField(max_length=255)
   # match_players = models.ManyToManyField(Player)
#    winner = models.ForeignKey(Player, related_name='match_winner', default='', on_delete=models.CASCADE)
 #   loser = models.ForeignKey(Player, related_name='match_loser', default='', on_delete=models.CASCADE)
  #  winning_score = models.PositiveIntegerField()
   # losing_score = models.PositiveIntegerField()
#    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
 #   def __str__(self):
  #      return self.name