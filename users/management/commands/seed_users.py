from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import Group, Permission
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = 'This command creates Users'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',
            '-n',
            default=1,
            type=int,
            help='How many users do you want to create?',
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {'is_staff': False, 'is_superuser': False})
        seeder.execute(inserted_entities={Group: [], Permission: []})
        return self.style.SUCCESS(f'{number} Users created!')
