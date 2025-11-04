import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class RoomType(models.Model):
    room_name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.room_name


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    arrive_date = models.DateField()
    departure_date = models.DateField()
    no_of_nights = models.IntegerField(validators=[MinValueValidator(1)])
    no_of_adults = models.IntegerField(validators=[MinValueValidator(1)])
    no_of_kids = models.IntegerField(blank=True)
    no_of_rooms = models.IntegerField(blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return (f'{self.last_name} - {self.email} - {self.arrive_date} - {self.departure_date} - {self.no_of_nights} - '
                f'{self.no_of_adults}')

    def clean(self):
        super().clean()

        today = timezone.localdate()  # dnešní datum podle nastavení TIME_ZONE

        if self.arrive_date <= today:
            raise ValidationError({'arrive_date': 'Datum příjezdu musí být alespoň zítra.'})
        if self.departure_date <= self.arrive_date:
            raise ValidationError({'departure_date': 'Datum odjezdu musí být alespoň den po příjezdu.'})
