from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    path('search/', views.search_id, name='search_id'),
    path('home/', views.home_page, name='home_page'),
    path('<int:match_id>/detail_view/', views.detail_view, name='detail_view'),
    path('dota2news/', views.dota2news, name='dota2news'),
]
