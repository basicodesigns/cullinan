from django.db import models

# Create your models here.
class Cottage(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    room = models.TextField()
    description = models.TextField()
   

    def __str__(self):
        return self.room[0:50]

