from __future__ import print_function
import requests
import json
import od_python
# from .forms import myForm
from od_python.rest import ApiException
from functools import reduce

api_instance = od_python.PlayersApi()


def account_data(account_id):
    global personaname, avatar
    try:
        # GET /players
        api_response = api_instance.players_account_id_get(account_id)
        personaname = api_response.profile.personaname
        avatar = api_response.profile.avatarfull
    except ApiException as e:
        print("Exception when calling BenchmarksApi->benchmarks_get: %s\n" % e)

    return personaname, avatar


# Recent Matches
def recentMatch(account_id):
    global recentmatches
    try:
        recentmatches = requests.get("https://api.opendota.com/api/players/" + str(account_id) + "/recentMatches")
        recentmatches = json.loads(recentmatches.text)
    except Exception as e:
        print("Cant get requests", e)

    return recentmatches


try:
    heroes = requests.get("https://api.opendota.com/api/heroes")
    heroes = json.loads(heroes.text)
except Exception as e:
    print("Cant get requests", e)


def winrate(recent):
    ranked = [5, 6, 7]
    ranked_match = [key for key in recent if key['lobby_type'] in ranked]
    radiant_win = [key['radiant_win'] for key in ranked_match]
    player_slot = [key['player_slot'] for key in ranked_match]
    ranked_match_count = len(ranked_match)
    win_count = 0
    for i in range(ranked_match_count):
        if player_slot[i] <= 127 and radiant_win[i]:
            win_count += 1
        elif player_slot[i] > 127 and not radiant_win[i]:
            win_count += 1
    return win_count, ranked_match_count


def match_detail(match_id):
    global match_data
    try:
        match_data = requests.get("https://api.opendota.com/api/matches/" + str(match_id))
        match_data = json.loads(match_data.text)
    except Exception as e:
        print("Cant get requests", e)

    return match_data


def radiant_total(datam):
    total = lambda x, y: x + y
    kills = reduce(total, [player['kills'] for player in datam['players'] if player['player_slot'] <= 127])
    deaths = reduce(total, [player['deaths'] for player in datam['players'] if player['player_slot'] <= 127])
    assists = reduce(total, [player['assists'] for player in datam['players'] if player['player_slot'] <= 127])
    total_golds = reduce(total,
                         [player['total_gold'] for player in datam['players'] if player['player_slot'] <= 127])
    gpm = reduce(total, [player['gold_per_min'] for player in datam['players'] if player['player_slot'] <= 127])
    xpm = reduce(total, [player['xp_per_min'] for player in datam['players'] if player['player_slot'] <= 127])
    lh = reduce(total, [player['last_hits'] for player in datam['players'] if player['player_slot'] <= 127])
    dn = reduce(total, [player['denies'] for player in datam['players'] if player['player_slot'] <= 127])
    hd = reduce(total, [player['hero_damage'] for player in datam['players'] if player['player_slot'] <= 127])
    td = reduce(total, [player['tower_damage'] for player in datam['players'] if player['player_slot'] <= 127])
    heal = reduce(total, [player['hero_healing'] for player in datam['players'] if player['player_slot'] <= 127])

    radiant_total_list = {
        'kills': kills,
        'deaths': deaths,
        'assists': assists,
        'total_golds': total_golds,
        'gpm': gpm,
        'xpm': xpm,
        'lh': lh,
        'dn': dn,
        'hd': hd,
        'td': td,
        'heal': heal,
    }  # kills, deaths, assists, total_golds, gpm, xpm, lh, dn, hd, td, heal

    return radiant_total_list


def dire_total(datam):
    total = lambda x, y: x + y
    kills = reduce(total, [player['kills'] for player in datam['players'] if player['player_slot'] > 127])
    deaths = reduce(total, [player['deaths'] for player in datam['players'] if player['player_slot'] > 127])
    assists = reduce(total, [player['assists'] for player in datam['players'] if player['player_slot'] > 127])
    total_golds = reduce(total,
                         [player['total_gold'] for player in datam['players'] if player['player_slot'] > 127])
    gpm = reduce(total, [player['gold_per_min'] for player in datam['players'] if player['player_slot'] > 127])
    xpm = reduce(total, [player['xp_per_min'] for player in datam['players'] if player['player_slot'] > 127])
    lh = reduce(total, [player['last_hits'] for player in datam['players'] if player['player_slot'] > 127])
    dn = reduce(total, [player['denies'] for player in datam['players'] if player['player_slot'] > 127])
    hd = reduce(total, [player['hero_damage'] for player in datam['players'] if player['player_slot'] > 127])
    td = reduce(total, [player['tower_damage'] for player in datam['players'] if player['player_slot'] > 127])
    heal = reduce(total, [player['hero_healing'] for player in datam['players'] if player['player_slot'] > 127])

    dire_total_list = {
        'kills': kills,
        'deaths': deaths,
        'assists': assists,
        'total_golds': total_golds,
        'gpm': gpm,
        'xpm': xpm,
        'lh': lh,
        'dn': dn,
        'hd': hd,
        'td': td,
        'heal': heal,
    }  # kills, deaths, assists, total_golds, gpm, xpm, lh, dn, hd, td, heal

    return dire_total_list


"""
match_id = {key['match_id'] for key in recentMatches}
player_slot = {key['match_id'] for key in recentMatches}
radiant_win = {key['radiant_win'] for key in recentMatches}
duration = {key['duration'] for key in recentMatches}
game_mode = {key['game_mode'] for key in recentMatches}
lobby_type = {key['lobby_type'] for key in recentMatches}
hero_id = {key['hero_id'] for key in recentMatches}
start_time = {key['start_time']for key in recentMatches}
version = {key['version'] for key in recentMatches}
kills = {key['kills'] for key in recentMatches}
deaths = {key['deaths'] for key in recentMatches}
assists = {key['assists'] for key in recentMatches}
skill = {key['skill'] for key in recentMatches}
lane = {key['match_id'] for key in recentMatches}
lane_role = {key['match_id'] for key in recentMatches}
is_roaming = {key['match_id'] for key in recentMatches}
cluster = {key['match_id'] for key in recentMatches}
leaver_status = {key['match_id'] for key in recentMatches}
party_size = {key['party_size'] for key in recentMatches}
tower_damage = {key['tower_damage'] for key in recentMatches}
xp_per_min = {key['xp_per_min'] for key in recentMatches}
gold_per_min = {key['gold_per_min'] for key in recentMatches}



"player_slot": 0,
"radiant_win": true,
"duration": 0,
"game_mode": 0,
"lobby_type": 0,
"hero_id": 0,
"start_time": 0,
"version": 0,
"kills": 0,
"deaths": 0,
"assists": 0,
"skill": 0,
"lane": 0,
"lane_role": 0,
"is_roaming": true,
"cluster": 0,
"leaver_status": 0,
"party_size": 0
"""
