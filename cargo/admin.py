from django.contrib import admin
from .models import Cargo, Car, Logistician, Driver, Company, PhoneNumber, Fuel

admin.site.register(Cargo)
admin.site.register(Car)
admin.site.register(Logistician)
admin.site.register(Driver)
admin.site.register(Company)
admin.site.register(PhoneNumber)
admin.site.register(Fuel)
# Register your models here.
