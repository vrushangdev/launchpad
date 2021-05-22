from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
POOL_CHOICE = (("Featured","Featured"),("Upcoming","Upcoming"))
POOL_TIER = (("Tier 1", "Tier 1"), ("Tier 2", "Tier 2"), ("Tier 3", "Tier 3"), ("Bonus Tier", "Bonus Tier"))
class Pool(models.Model):
    pool_name = models.CharField(max_length=100,unique=True)
    pool_access = models.CharField(max_length=100,choices=POOL_CHOICE,default="Upcoming")
    pool_status = models.BooleanField()
    swap_amount = models.CharField(max_length=100)
    pool_min_amount = models.CharField(max_length=100,unique=False)
    pool_max_amount = models.CharField(max_length=100,unique=False)
    pool_progress = models.IntegerField(default=0, validators= [MinValueValidator(1), MaxValueValidator(100)])
    pool_address = models.CharField(max_length=100,unique=True)
    pool_tier = models.CharField(max_length=100,choices=POOL_TIER,default="Tier 1")
    pool_raised_amount = models.CharField(max_length=100, unique=False)
    pool_coin_symbol = models.CharField(max_length=100, unique=False)
    pool_coin_name = models.CharField(max_length=100, unique=False)
    pool_coin_decimal = models.CharField(max_length=100, unique=False)
    pool_coin_total_supply = models.CharField(max_length=100, unique=False)
    

    def __str__(self):
    	return "{} | {}".format(self.pool_name, self.pool_tier)


class Whitelist(models.Model):
    eth_address = models.CharField(max_length=100,unique=False)
    pool_name = models.ForeignKey(to=Pool, on_delete=models.CASCADE)

