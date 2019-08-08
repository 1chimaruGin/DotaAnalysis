# from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from .forms import RegisterForm, LoginForm, SearchForm
from django.contrib.auth import authenticate, login
from .opendota import account_data, recentMatch, heroes, winrate, match_detail, radiant_total, dire_total
from django.contrib.auth.decorators import login_required
import datetime


def register(request):
    # print(request.method)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'web_templates/reg_form.html', {'form': form})


def login_user(request):
    errors = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('search_id')
            errors = 'Username or Password incorrect!'
    else:
        form = LoginForm()
    return render(request, 'web_templates/login.html', {'form': form, 'errors': errors})


@login_required
def search_id(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            request.session['steam_id'] = form.cleaned_data['steam_id']
            return redirect('home_page')
    else:
        form = SearchForm()
    return render(request, 'web_templates/id_search.html', {'form': form})


@login_required()
def home_page(request):
    account_id = int(request.session.get('steam_id'))
    personaname, avatar = account_data(account_id)
    kwargs = {'personaname': personaname, 'avatar': avatar}
    this_week = datetime.datetime.now().timestamp()
    prev_week = datetime.datetime.now() - datetime.timedelta(days=7)
    same_week = True if datetime.datetime.now().month is prev_week.month else False

    prev_week = prev_week.timestamp()
    recentMatches = recentMatch(account_id)
    win_count, match_count = winrate(recentMatches)
    new_dict = {
                'recentMatches': recentMatches, 'heroes': heroes, 'match_count': match_count, 'win_count': win_count,
                'loss_count': match_count - win_count,
                'winrate': round((win_count / match_count) * 100, 2), 'mmr_diff': (win_count - (match_count - win_count)) * 25,
                'this_week': this_week,
                'prev_week': prev_week,
                'same_week': same_week,
    }
    kwargs.update(new_dict)
    return render_to_response('web_templates/home_page.html', kwargs)


@login_required
def detail_view(request, match_id):
    personaname, avatar = account_data(int(request.session.get('steam_id')))
    kwargs = {'personaname': personaname, 'avatar': avatar}
    match_data = match_detail(match_id)
    radiant = radiant_total(match_data)
    dire = dire_total(match_data)
    new_dict = {
        'match_data': match_data,
        'heroes': heroes,
        'account_id': int(request.session.get('steam_id')),
        'radiant': radiant,
        'dire': dire,
    }
    kwargs.update(new_dict)
    return render(request, 'web_templates/player_detail_view.html', kwargs)


@login_required
def dota2news(request):
    personaname, avatar = account_data(int(request.session.get('steam_id')))
    kwargs = {'personaname': personaname, 'avatar': avatar}
    return render(request, 'web_templates/dota_news.html', kwargs)


