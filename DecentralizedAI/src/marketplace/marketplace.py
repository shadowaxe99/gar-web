
import django
from django.db import models

class Marketplace(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='marketplaces', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    marketplace = models.ForeignKey(Marketplace, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    item = models.ForeignKey(Item, related_name='transactions', on_delete=models.CASCADE)
    buyer = models.ForeignKey('auth.User', related_name='purchases', on_delete=models.CASCADE)
    seller = models.ForeignKey('auth.User', related_name='sales', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer} bought {self.item} from {self.seller} on {self.transaction_date}'
