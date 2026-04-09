from django.contrib import admin
from .models import Customer, Vehicle
from .models import Reservation

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Reservation)