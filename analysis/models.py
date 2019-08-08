# from datetime import datetime
# from datetime import timedelta
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, User
)

# from django.db.models import Q
# from django.core import serializers
# from django.core.exceptions import ObjectDoesNotExist
# from django.conf import settings
# from django.utils.timezone import get_current_timezone
# from django.utils import timezone


class UserForm(models.Model):
    name = models.CharField(max_length=100)
    steam_id = models.CharField(max_length=10)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    steam_id = models.CharField(max_length=10)
    password = models.CharField(max_length=100)


'''
{'assists': 15,
  'cluster': 156,
  'deaths': 9,
  'duration': 2632,
  'game_mode': 22,
  'gold_per_min': 478,
  'hero_damage': 32830,
  'hero_healing': 0,
  'hero_id': 68,
  'is_roaming': False,
  'kills': 9,
  'lane': 2,
  'lane_role': 2,
  'last_hits': 143,
  'leaver_status': 0,
  'lobby_type': 7,
  'match_id': 4936351290,
  'party_size': 5,
  'player_slot': 131,
  'radiant_win': True,
  'skill': None,
  'start_time': 1564502514,
  'tower_damage': 546,
  'version': 21,
  'xp_per_min': 617}
'''


