from django.contrib import admin

from .models import Cottage, Room, CottageImages

# Register your models here.
admin.site.register(Cottage)
admin.site.register(Room)
admin.site.register(CottageImages)