from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game'),
    path('collect/', views.collect_wood, name='collect_wood'),
    path('update_wood/', views.update_wood, name='update_wood'),

]

