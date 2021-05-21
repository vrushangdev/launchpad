from django.db import models

# Create your models here.
POOL_CHOICE = (("Featured","Featured"),("Upcoming","Upcoming"))

class Pool(models.Model):
    pool_name = models.CharField(max_length=100,unique=True)
    pool_access = models.CharField(max_length=100,choices=POOL_CHOICE,default="Upcoming")
    pool_status = models.BooleanField()
    swap_amount = models.CharField(max_length=100)
    pool_adress = models.CharField(max_length=100,unique=True)


class Whitelist(models.Model):
    eth_adddress = models.CharField(max_length=100,unique=True)
    pool_name = models.ForeignKey(to=Pool, on_delete=models.CASCADE)
