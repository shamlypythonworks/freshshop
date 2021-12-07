from django.db import models
from homeapp . models import *
# Create your models here.
class cartlist(models.Model):
    cart_id = models.CharField(max_length=100,unique=True,primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.cart_id
class cartitems(models.Model):
    prokee = models.ForeignKey(prdttable,on_delete=models.CASCADE)
    listkee = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.prokee
    def amount_each(self):
       total_each = (self.quan * self.prokee.price)
       return total_each