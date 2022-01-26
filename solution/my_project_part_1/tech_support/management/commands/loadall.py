import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create fixtures from json file," "createfixtures [filename] [app.model]"

    def handle(self, *args, **options):
        # tech_support fixtures:
        os.system("python manage.py loaddata fixtures/tech_support.json")
        # courses fixtures:
        os.system("python manage.py loaddata fixtures/courses.json")
        # cars fixtures:
        os.system("python manage.py loaddata fixtures/cars.json")
