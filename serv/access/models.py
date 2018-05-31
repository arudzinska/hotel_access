from django.db import models


class Customer(models.Model):
    """ Customer (both guests and non-guests) model """

    name = models.CharField(max_length=100)
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
    """ Rule model describing the conditions to enter an area.

    'area' many-to-many field creates a 'hidden' join table which may be complicated
    to reach manually, but for the purpose of this app it is sufficient. """

    area = models.ManyToManyField(Area)
    can_access = models.BooleanField()
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    price = models.FloatField(null=True)
    for_guests = models.NullBooleanField()
    adult = models.NullBooleanField()
    weekend = models.NullBooleanField()
    visited_this_day = models.ForeignKey(Area, on_delete=models.SET_NULL, related_name='+', null=True)
    free_per_stay = models.PositiveIntegerField(null=True)

    def __str__(self):
        return u'area: {}, can access: {}, from(time): {}, to(time): {}, from(date): {}, to(date) {}, price: {}, for guests: {}, adult: {}, weekend: {}, visited that day:{}, free_per_stay: {}'.format(self.area, self.can_access, self.from_time, self.to_time, self.from_date, self.to_date, self.price, self.for_guests, self.adult, self.weekend, self.visited_this_day, self.free_per_stay)


class Logs(models.Model):
    """ Model for visits logs. """

    name = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='+')
    date = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.SET_NULL(), related_name='+')