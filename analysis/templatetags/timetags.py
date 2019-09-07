from django import template
from analysis.performance_analysis import rank_tier
import time

register = template.Library()


def print_timestamp(timestamp):
    right_now = time.time()
    ts = float(right_now) - float(timestamp)
    if ts < 86400:
        return str(round(ts/3600))+' hours ago'
    elif ts < 172800:
        return '{:d}'.format(int(ts/86400))+' day ago'
    else:
        return '{:d}'.format(int(ts/86400))+' days ago'


def print_week(timestamp):
    ts = float(timestamp)
    return time.strftime('%d', time.gmtime(ts))


def print_month(timestamp):
    ts = float(timestamp)
    return time.strftime("%b", time.gmtime(ts))


def net_format(gold):
    net_worth = float(gold) / 1000
    return '{:.1f}'.format(net_worth)


register.filter(print_timestamp)
register.filter(print_week)
register.filter(print_month)
register.filter(net_format)
