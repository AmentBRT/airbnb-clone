import random
from typing import Any
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandParser
from django.utils import timezone
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models
from reservations import models as reservations_models


class Command(BaseCommand):
    help = 'This command creates Reserations'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',
            '-n',
            default=1,
            type=int,
            help='How many reservations do you want to create?',
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        now = timezone.now().date()
        seeder = Seed.seeder()
        seeder.add_entity(
            reservations_models.Reservation,
            number,
            {
                'status': lambda x: random.choice(reservations_models.Reservation.Status.values),
                'check_in': lambda x: now,
                'check_out': lambda x: now + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute(
            inserted_entities={
                users_models.User: [u.id for u in users_models.User.objects.all()],
                rooms_models.Room: [r.id for r in rooms_models.Room.objects.all()],
            }
        )
        return self.style.SUCCESS(f'{number} Reserations created!')
