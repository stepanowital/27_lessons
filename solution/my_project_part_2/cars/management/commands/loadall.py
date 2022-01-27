import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create fixtures from json file," "createfixtures [filename] [app.model]"

    def handle(self, *args, **options):
        # cars fixtures:
        os.system("python manage.py loaddata fixtures/cars.json")
