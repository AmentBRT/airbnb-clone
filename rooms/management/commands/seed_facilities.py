from typing import Any
from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = 'This command creates Facilities'

    def handle(self, *args: Any, **options: Any) -> str | None:
        facilities_names = [
            'Private entrance',
            'Paid parking on premises',
            'Paid parking off premises',
            'Elevator',
            'Parking',
            'Gym',
        ]
        facilities = map(lambda name: Facility(name=name), facilities_names)
        Facility.objects.bulk_create(facilities)
        return self.style.SUCCESS(f'{len(facilities_names)} Amenities Created!')
