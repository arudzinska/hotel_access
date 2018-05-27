from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Customer(models.Model):
    """ Customer (both guests and non-guests) model """
    name = models.CharField(max_length=100)
    #description = models.CharField(max_length=1000)
    #slogan = models.CharField(max_length=500)
    #founded_date = models.CharField(max_length=500)
    balance = models.FloatField()
    birth = models.DateField()
    is_guest = models.BooleanField()

    def __str__(self):
        return u'{}, {}, guest: {}, {}e'.format(self.name, self.birth, self.is_guest, self.balance)

class Area(models.Model):
    """ Hotel area model """
    name = models.CharField(max_length=100)

    def __str__(self):
        return u'{}'.format(self.name)

class Rule(models.Model):
    """ Rule model describing the conditions to enter an area """
    area = models.ManyToManyField(Area)
    can_access = models.BooleanField()
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    on_date = models.DateField(null=True)
    for_guests = models.NullBooleanField()
    adult = models.NullBooleanField()
    weekend = models.NullBooleanField()
    visited_this_day = models.ForeignKey(Area, on_delete=models.SET_NULL, related_name='+', null=True)

    def __str__(self):
        return u'area: {}, can access: {}, from(time): {}, to(time): {}, on(date): {}, for guests: {}, adult: {}, weekend: {}, visited that day:{}'.format(self.area, self.can_access, self.from_time, self.to_time, self.on_date, self.for_guests, self.adult, self.weekend, self.visited_this_day)


# class Store(models.Model):
#     """ Store location model.  Foreign key to Chain."""
#     chain = models.ForeignKey(Chain)
#     number = models.CharField(max_length=20)
#     address = models.CharField(max_length=1000)
#     opening_date = models.DateTimeField(default=timezone.now)
#
#     # Business hours in a 24 hour clock.  Default 8am-5pm.
#     business_hours_start = models.IntegerField(
#         default=8,
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(23)
#         ]
#     )
#     business_hours_end = models.IntegerField(
#         default=17,
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(23)
#         ]
#     )