from celery import shared_task
from .models import Player
from datetime import datetime

@shared_task
def generate_wood():
    # Aquí actualizamos la madera de todos los jugadores.
    players = Player.objects.all()
    for player in players:
        player.wood += player.trees_per_second  # Añadimos la madera generada por segundo
        player.save()

    return f"Generated wood for {len(players)} players at {datetime.now()}"
