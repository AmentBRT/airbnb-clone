from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models
from lists import models as lists_models


class Command(BaseCommand):
    help = 'This command creates Lists'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',
            '-n',
            default=1,
            type=int,
            help='How many lists do you want to create?',
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(lists_models.List, number)
        seeder.execute(
            inserted_entities={
                users_models.User: [u.id for u in users_models.User.objects.all()],
                rooms_models.Room: [r.id for r in rooms_models.Room.objects.all()],
            }
        )
        return self.style.SUCCESS(f'{number} Lists created!')
