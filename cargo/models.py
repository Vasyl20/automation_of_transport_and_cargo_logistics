from django.db import models
# Create your models here.
class Cargo(models.Model):
    SPECIAL_CODE_CHOICES = (
        ('bullin', 'bullin'),
        ('folls', 'folls'),
    )

    special_code = models.CharField(max_length=10)
    cargo_name = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=200)
    cargo_tonnage = models.DecimalField(max_digits=8, decimal_places=2)
    cargo_volume = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    mileage = models.DecimalField(max_digits=8, decimal_places=2)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    payment_card = models.BooleanField(default=False,null=True, blank=True ,verbose_name='Оплата карткою')
    payment_cash = models.BooleanField(default=False,null=True, blank=True ,verbose_name='Оплата готівкою')
    payment_non_cash = models.BooleanField(default=False,null=True, blank=True, verbose_name='Оплата безготівково')
    loading_start = models.BooleanField(default=False, null=True, blank=True)
    cargo_loaded = models.BooleanField(default=False, null=True, blank=True)
    loaded_car_departed = models.BooleanField(default=False, null=True, blank=True)
    car_in_transit = models.BooleanField(default=False, null=True, blank=True)
    unloading_arrived = models.BooleanField(default=False, null=True, blank=True)
    cargo_unloaded = models.BooleanField(default=False, null=True, blank=True)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    logistician = models.ForeignKey('Logistician', on_delete=models.CASCADE)



class Car(models.Model):
    special_code = models.CharField(max_length=10)
    registration_number = models.CharField(max_length=20)
    year = models.IntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    commercial_description = models.CharField(max_length=200)
    vehicle_identification_number = models.CharField(max_length=50)
    total_weight = models.DecimalField(max_digits=8, decimal_places=2)
    unloaded_weight = models.DecimalField(max_digits=8, decimal_places=2)
    engine_volume = models.DecimalField(max_digits=8, decimal_places=2)
    fuel_type = models.ForeignKey('Fuel', on_delete=models.CASCADE)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model} {self.registration_number}"



class Logistician(models.Model):
    special_code = models.CharField(max_length=10)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_numbers = models.ManyToManyField('PhoneNumber')
    order_count = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Driver(models.Model):
    special_code = models.CharField(max_length=10)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    driver_license = models.CharField(max_length=20)
    phone_numbers = models.ManyToManyField('PhoneNumber')
    address = models.CharField(max_length=200)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Company(models.Model):
    special_code = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)
    director_name = models.CharField(max_length=100, null=True, blank=True)
    director_phone = models.CharField(max_length=20, null=True, blank=True)
    director_email = models.EmailField(null=True, blank=True)
    manager_telegram = models.CharField(max_length=100, null=True, blank=True)
    manager_name = models.CharField(max_length=100, null=True, blank=True)
    manager_phone = models.CharField(max_length=20, null=True, blank=True)
    manager_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.number

class Fuel(models.Model):
    special_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name