from django.db import models

from movies.models import MultiSelectField


# Create your models here.

from movies.models import BaseClass

class DeviceChoices(models.TextChoices):

    ALL = 'ALL Devices','All Devices'

    PHONE ='Phone','Phone'

    TABLET ='Tablet','Tablet'

    TV ='TV','TV'

    LAPTOP ='Laptop','Laptop'

class QualityChoices(models.TextChoices):

    P480 ='480p','480p'

    P1080 ='Upto 1080p','Upto 1080p'

    P4k ='Upto 4k','Upto 4k'

class ScreenOrDownloadDevicesChoices(models.IntegerChoices):

    ONE =1,'1'

    TWO =2,'2'

    FOUR =4,'4'


class SubscriptionPlans(BaseClass):

    name = models.CharField(max_length=25)

    amount = models.FloatField()

    devices = MultiSelectField(choices=DeviceChoices.choices)

    quality = models.CharField(max_length=30,choices=QualityChoices.choices)

    no_of_screens = models.IntegerField(choices=ScreenOrDownloadDevicesChoices.choices)

    download_devices = models.IntegerField(choices=ScreenOrDownloadDevicesChoices.choices)


    class META :

        verbose_name ='Subscription Plans'

        verbose_name_Plural ='Subscription Plans'

    def __str__(self):

        return self.name


