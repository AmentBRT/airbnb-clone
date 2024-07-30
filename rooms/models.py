from django.db import models
from django_countries import fields as countries_fields
from core import models as core_models
from users import models as users_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item Model"""

    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class RoomType(AbstractItem):
    """Room Type Model"""

    class Meta:
        verbose_name = 'Room Type'


class Amenity(AbstractItem):
    """Amenity Model"""

    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(AbstractItem):
    """Facility Model"""

    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):
    """House Rule Model"""

    class Meta:
        verbose_name = 'House Rule'


class Room(core_models.TimeStampedModel):
    """Room Model"""

    host = models.ForeignKey(
        users_models.User,
        on_delete=models.CASCADE,
        related_name='rooms',
    )
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.SET_NULL,
        related_name='rooms',
        null=True,
    )
    amenities = models.ManyToManyField(Amenity, related_name='rooms', blank=True)
    facilities = models.ManyToManyField(Facility, related_name='rooms', blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name='rooms', blank=True)
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = countries_fields.CountryField()
    city = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=140)
    guests = models.PositiveSmallIntegerField()
    beds = models.PositiveSmallIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    baths = models.PositiveSmallIntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Photo(core_models.TimeStampedModel):
    """Photo Model"""

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='photos')
    caption = models.CharField(max_length=80)
    file = models.ImageField()

    def __str__(self) -> str:
        return self.caption
