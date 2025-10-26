from django.db import models


class RoomType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    arrive_date = models.DateField()
    departure_date = models.DateField()
    no_of_nights = models.IntegerField()
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    no_of_rooms = models.IntegerField()
    room_type = models.ManyToManyField(RoomType)
    description = models.TextField()