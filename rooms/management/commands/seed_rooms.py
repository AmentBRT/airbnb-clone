import random
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):
    help = 'This command creates Rooms'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',
            '-n',
            default=1,
            type=int,
            help='How many rooms do you want to create?',
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()
        users = users_models.User.objects.all()[:50]
        room_types = rooms_models.RoomType.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                'name': lambda x: seeder.faker.address(),
                'host': lambda x: random.choice(users),
                'room_type': lambda x: random.choice(room_types),
                'price': lambda x: random.randint(1, 300),
                'guests': lambda x: random.randint(1, 20),
                'beds': lambda x: random.randint(1, 5),
                'bedrooms': lambda x: random.randint(1, 5),
                'baths': lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute(
            inserted_entities={
                rooms_models.Amenity: [a.id for a in rooms_models.Amenity.objects.all()],
                rooms_models.Facility: [f.id for f in rooms_models.Facility.objects.all()],
                rooms_models.HouseRule: [hr.id for hr in rooms_models.HouseRule.objects.all()],
            }
        )
        created_rooms = flatten(created_rooms[rooms_models.Room])
        for id in created_rooms:
            room = rooms_models.Room.objects.get(id=id)
            photos = [
                rooms_models.Photo(
                    caption=seeder.faker.sentence(),
                    file=f'/room-photos/{random.randint(1, 10):02d}.jpeg',
                    room=room,
                )
                for _ in range(random.randint(3, 7))
            ]
            rooms_models.Photo.objects.bulk_create(photos)
        return self.style.SUCCESS(f'{number} Rooms created!')
