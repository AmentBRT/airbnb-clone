import random
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models
from reviews import models as reviews_models


class Command(BaseCommand):
    help = 'This command creates Reviews'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',
            '-n',
            default=1,
            type=int,
            help='How many reviews do you want to create?',
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                'accuracy': lambda x: random.randint(1, 5),
                'communication': lambda x: random.randint(1, 5),
                'cleanliness': lambda x: random.randint(1, 5),
                'location': lambda x: random.randint(1, 5),
                'check_in': lambda x: random.randint(1, 5),
                'value': lambda x: random.randint(1, 5),
            },
        )
        seeder.execute(
            inserted_entities={
                users_models.User: [u.id for u in users_models.User.objects.all()],
                rooms_models.Room: [r.id for r in rooms_models.Room.objects.all()],
            }
        )
        return self.style.SUCCESS(f'{number} Reviews created!')
