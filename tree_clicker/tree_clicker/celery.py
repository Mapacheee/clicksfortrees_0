from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Establecer el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree_clicker.settings')

app = Celery('tree_clicker')

# Usar una cadena para que Celery pueda encontrar la configuración automáticamente
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar tareas de todas las aplicaciones Django configuradas en INSTALLED_APPS
app.autodiscover_tasks()

# Configuración de Celery
app = Celery('tree_clicker')

# Agregar la tarea periódica
app.conf.beat_schedule = {
    'generate-wood-every-second': {
        'task': 'clicker.tasks.generate_wood',
        'schedule': crontab(second='*/1'),  # Ejecutar cada segundo
    },
}

# Cargar la configuración y tareas
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
