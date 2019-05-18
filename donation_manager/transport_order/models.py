from django.db import models
# from address.models import AddressField

from donation_manager.users.models import User
from donation_manager.donation.models import Donation


# Create your models here.

class Transport_Order(models.Model):

    WAITING_DESTINATION_DEFINITION = 'WDTN'
    WAITING_DRIVER_ASSIGNMENT = 'WDRV'
    PICKUP_SCHEDULED = "PSCH"
    IN_TRANSIT = "TRAN"
    DELIVERED = "DLVR"

    TRANSIT_STATUS_CHOICES = (
        (WAITING_DESTINATION_DEFINITION, "Waiting for Destination Definition"),
        (WAITING_DRIVER_ASSIGNMENT, "Waiting for assigning a driver"),
        (PICKUP_SCHEDULED, "Pickup Scheduled"),
        (IN_TRANSIT, "In Transit"),
        (DELIVERED, "Delivered")
    )

    driver = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    donated_item = models.ForeignKey(Donation, on_delete=models.SET_NULL, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    destination = models.CharField(max_length=200, blank=True, null=True)
    transit_status = models.CharField(
        max_length=4,
        choices=TRANSIT_STATUS_CHOICES
    )
    agreed_weekday = models.OneToOneField("Week_Day", related_name='weekday_assigned', on_delete=models.SET_NULL, blank=True, null=True)
    agreed_time_window = models.OneToOneField("Time_Window", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.donated_item.name + ' from: ' + self.origin + ' to: ' + self.destination
    

    @staticmethod
    def get_all_waiting_destination():

        queryset = Transport_Order.objects.filter(transit_status=Transport_Order.WAITING_DESTINATION_DEFINITION)

        return queryset

    @staticmethod
    def get_all_waiting_driver_assignment():
        
        queryset = Transport_Order.objects.filter(transit_status=Transport_Order.WAITING_DRIVER_ASSIGNMENT)

        return queryset


    

class Week_Day(models.Model):

    MO = 'MO'
    TU = 'TU'
    WE = 'WE'
    TH = 'TH'
    FR = 'FR'
    SA = 'SA'
    SU = 'SU'

    DAYS_OF_WEEK = (
        (MO, 'Monday'),
        (TU, 'Tuesday'),
        (WE, 'Wednesday'),
        (TH, 'Thursday'),
        (FR, 'Friday'),
        (SA, 'Saturday'),
        (SU, 'Sunday')
    )

    transport_order = models.ForeignKey(Transport_Order, on_delete=models.CASCADE)
    day_of_week = models.CharField(
        max_length=2,
        choices=DAYS_OF_WEEK
    )


class Time_Window(models.Model):

    AM_6_to_8 = "06:00 AM - 08:00 AM"
    AM_8_to_10 = "08:00 AM - 10:00 AM"
    AM_10_to_Noon = "10:00 AM - Noon"
    PM_02_to_04 = "02:00 PM - 04:00 PM"
    PM_04_to_06 = "04:00 PM - 06:00 PM"
    PM_06_to_08 = "06:00 PM - 08:00 PM" 

    TIME_WINDOWS = (
        (AM_6_to_8, "06:00 AM - 08:00 AM"),
        (AM_8_to_10, "08:00 AM - 10:00 AM"),
        (AM_10_to_Noon, "10:00 AM - Noon"),
        (PM_02_to_04, "02:00 PM - 04:00 PM"),
        (PM_04_to_06, "04:00 PM - 06:00 PM"),
        (PM_06_to_08, "06:00 PM - 08:00 PM"),
    )

    week_day = models.ForeignKey(Week_Day, on_delete=models.CASCADE)

    time = models.CharField(
        max_length=20,
        choices=TIME_WINDOWS
    )
