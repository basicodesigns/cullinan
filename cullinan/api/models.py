from django.db import models


class Cottage(models.Model):
    name = models.TextField(null=True, blank=True, max_length=30)
    description = models.TextField(null=True, blank=True, max_length=255)
    bedrooms = models.IntegerField()
    booked = models.BooleanField()
    cost = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name
# Create your models here.


class CottageImages(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True, max_length=30)
    description = models.TextField(null=True, blank=True, max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Room(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    room = models.TextField()
    description = models.TextField()
   

    def __str__(self):
        return self.room[0:50]

