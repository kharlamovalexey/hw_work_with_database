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
            try:
                Phone.objects.create(**phone)
                self.stdout.write(self.style.SUCCESS(f'Объект {phone} сохранен в БД'))
            except:
                self.stdout.write(self.style.ERROR(f'Не удалось вставить объект {phone}'))

        
