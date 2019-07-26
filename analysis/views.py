# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import myForm


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            steam_id = form.cleaned_data['steam_id']
            if (name == 'ichimaru') and (steam_id == '321411772'):
                return render(request, 'web_templates/home_page.html', {'form': form})
            else:
                error = 'User name or Steam ID did not match'
                form = myForm()
                args = {'error': error, 'form': form}
                return render(request, 'web_templates/register.html', args)
    else:
        form = myForm()

    return render(request, 'web_templates/register.html', {'form': form})


def index(request):
    form = ''
    return render(request, 'web_templates/home_page.html', {'form': form})


def home_page(request):
    form = ''
    return render(request, 'web_templates/home_page.html', {'form': form})


def detail_view(request):
    form = ''
    return render(request, 'web_templates/player_detail_view.html', {'form': form})


def dota2news(request):
    form = ''
    return render(request, 'web_templates/dota_news.html', {'form': form})
