import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_data = Phone(
                id = phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=float(phone['price']),
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
            )
            phone_data.save()
            self.stdout.write(self.style.SUCCESS(f"Phone '{phone_data}' created successfully."))