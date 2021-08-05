from django.db import models


class Cottage(models.Model):
    name = models.TextField()
    description = models.TextField()
    bedrooms = models.IntegerField()
    booked = models.BooleanField()

    def __str__(self):
        return self.name
# Create your models here.


class CottageImages(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Room(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    room = models.TextField()
    description = models.TextField()
   

    def __str__(self):
        return self.room[0:50]

