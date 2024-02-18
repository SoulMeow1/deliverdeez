from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
    
class PartTimer(models.Model):
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
    
class Delivery(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    #uuid?
    staff = models.ForeignKey(Staff, null = True, on_delete = models.SET_NULL)
    partTimer = models.ForeignKey(PartTimer, null = True, blank = True, on_delete = models.SET_NULL)
    itemName = models.CharField(max_length = 200, null = True)
    itemDescription = models.CharField(max_length = 200, null = True)
    pickUpLocation = models.CharField(max_length = 200, null = True)
    dropOffLocation = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)

    def __str__(self):
        it = "item: "
        pu = ". pick up: "
        dr = ". drop off: "

        return it + self.itemName + pu + self.pickUpLocation + dr + self.dropOffLocation