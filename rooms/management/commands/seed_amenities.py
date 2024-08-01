from typing import Any
from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = 'This command creates Amenities'

    def handle(self, *args: Any, **options: Any) -> str | None:
        amenities_names = [
            'Wifi',
            'Kitchen',
            'Washer',
            'Dryer',
            'Air conditioning',
            'Heating',
            'Dedicated workspace',
            'TV',
            'Hair dryer',
            'Iron',
            'Pool',
            'Hot tub',
            'Free parkin',
            'EV charger',
            'Crib',
            'King bed',
            'Gym',
            'BBQ grill',
            'Breakfast',
            'Indoor fireplace',
            'Smoking allowed',
            'Beachfront',
            'Waterfront',
            'Ski-in/ski-out',
            'Smoke alarm',
            'Carbon monoxide alarm',
        ]
        amenities = map(lambda name: Amenity(name=name), amenities_names)
        Amenity.objects.bulk_create(amenities)
        return self.style.SUCCESS(f'{len(amenities_names)} Amenities Created!')
