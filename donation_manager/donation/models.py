from django.db import models
from donation_manager.users.models import User
from address.models import AddressField


class Institution(models.Model):
    name = models.CharField(max_length=50)
    address = AddressField(on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    users = models.ManyToManyField(User)


class Donee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = AddressField(on_delete=models.CASCADE)


class Donation(models.Model):

    WAITING_CLAIM = 'WC'
    CLAIMED = 'CL'
    IN_STOCK = 'ST'
    ALLOCATED_DONATION = 'AD'
    DONATED = 'DT'
    LOST_STOLEN = 'LS'
    DAMAGED_EXPIRED = 'DE'

    DONATION_STATUS_CHOICES = (
        (WAITING_CLAIM, 'Waiting for claim'),
        (CLAIMED, 'Claimed'),
        (IN_STOCK, 'In Stock'),
        (ALLOCATED_DONATION, 'Allocated for donation'),
        (DONATED, 'Donated'),
        (LOST_STOLEN, 'Lost / Stolen'),
        (DAMAGED_EXPIRED, 'Damaged / Expired'),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    weight = models.FloatField(blank=True, null=True)
    dimension = models.CharField(max_length=50)
    status = models.CharField(
        max_length=2,
        choices=DONATION_STATUS_CHOICES,
        default=WAITING_CLAIM,
    )
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    donee = models.ForeignKey(Donee, on_delete=models.SET_NULL, blank=True, null=True)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False)